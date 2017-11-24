import pyglet
from pyglet.window import key
from time import time, sleep

import math

from .informations import Informations
from .fps import Fps
from .cart import Cart
from .rail import Rail
from .pole import Pole
from .axle import Axle

from .system.calculating import inverted
import graphic.system.parameters as cnst


class Application(pyglet.window.Window):
    def __init__(self, gui=True):

        # pour s'occuper de la boucle et des episodes
        self.fps = cnst.fps
        self.dt = 1 / cnst.fps

        self.initState()

        self.alive = True
        self.episode = 0
        print('ep', self.episode)

        self.gui = gui

        if self.gui:
            self.initScreen()

            # on prépare la fenetre
            self.initWindow()

    def initState(self):
        self.x = cnst.x0
        self.v = cnst.v0
        self.a = cnst.a0
        self.θ = cnst.θ0
        self.ω = cnst.ω0
        self.α = cnst.α0

    def initScreen(self):
        # recuperation des informations de display
        platform = pyglet.window.get_platform()
        display = platform.get_default_display()
        screen = display.get_default_screen()
        screen_width = screen.width
        screen_height = screen.height

        # on init la fenetre
        super(Application, self).__init__(screen=screen,
                                          width=cnst.screen_width_px,
                                          height=cnst.screen_height_px,
                                          caption='Simulation',
                                          vsync=False)

        # on le met la window au centre de l'ecran
        # x_win, y_win = self.get_location()
        self.set_location((screen_width - self.width) // 2,
                          (screen_height - self.height) // 2)

        # pour changer le bg
        # pyglet.gl.glClearColor(1, 1, 1, 1)

    def initWindow(self):

        # pour permettre a l'utilisateur de bouger lui meme
        self.userForce = 0

        # coefficient pour la mise à l'echelle
        self.scale = cnst.screen_width_px / (cnst.x_threshold * 2)  # px / m

        # init du batch et grp pour le render
        self.myBatch = pyglet.graphics.Batch()
        self.background = pyglet.graphics.OrderedGroup(0)
        self.midground = pyglet.graphics.OrderedGroup(1)
        self.foreground = pyglet.graphics.OrderedGroup(2)

        # init des elements graphique
        self.fps = Fps(self, rate=1)

        self.informations = Informations(self)

        self.rail = Rail(self)

        self.cart = Cart(self,
                         x0=self.x,
                         longueur=(self.scale * cnst.width_cart),
                         largeur=(self.scale * cnst.length_cart))

        self.pole = Pole(self,
                         x0=self.x,
                         θ0=self.θ,
                         longueur=(self.scale * cnst.length_pole),
                         largeur=(self.scale * cnst.width_pole))

        self.axle = Axle(self,
                         x0=self.x,
                         radius=(0.35 * self.scale * cnst.width_pole))

        # pour les 60fps
        self.last = time()
        # pour refresh toutes les 10 secondes
        self.count = 0

    def reset(self):
        self.episode += 1
        print('ep', self.episode)

        self.initState()

        # init de la fenetre

        self.fps.x = self.x

        self.cart.resetPositon()

        self.pole.x = self.x
        self.pole.θ = self.θ + (cnst.pi / 2)

        self.axle.resetPosition()

        self.last = time()
        # pour refresh toutes les 10 secondes
        self.count = 0

    # fonction liée au controle de la fenetre
    def on_draw(self):
        self.render()

    def on_close(self):
        self.alive = False

    def on_key_press(self, symbol, modifiers):

        if symbol == key.LEFT:
            self.userForce = -1

        elif symbol == key.RIGHT:
            self.userForce = 1

        elif symbol == key.SPACE:
            sleep(1)

        elif symbol == key.ENTER:
            self.reset()

    def on_key_release(self, symbol, modifiers):

        if symbol == key.LEFT or symbol == key.RIGHT:
            self.userForce = 0

    def render(self):
        self.count += 1

        self.limitFps()

        self.clear()
        self.myBatch.draw()

        self.dispatch_events()
        self.flip()

    def limitFps(self):
        dtFrames = (time() - self.last)
        if dtFrames < self.dt:  # si on est trop en avance
            sleep(self.dt - dtFrames)
        self.last = time()

    def step(self, A):

        if self.gui and self.userForce != 0:
            A = self.userForce  # mode user control

        next_state, dx, dθ = inverted(A, self.extState)
        self.updateStates(next_state)

        done = self.done

        if self.gui:
            if done:
                self.reset()
            else:
                self.update(dx * self.scale, dθ)
            self.render()

        else:
            if done:
                self.initState()

        return next_state, self.reward, done

    def update(self, dx_px, dθ):
        '''prends en parametre une variation en px'''

        # translation suivant x
        self.cart.translation(dx_px)
        self.pole.translation(dx_px)
        self.axle.translation(dx_px)

        # rotation
        self.pole.rotation(dθ)

        # display des states
        if self.count > 5:
            self.informations.label.text = self.informations.formatStates(self.state)
            self.count = 0

            # self.frames += 1

    # fonction externe
    def updateStates(self, states):
        self.x = states[0]
        self.v = states[1]
        self.a = states[2]
        self.θ = states[3]
        self.ω = states[4]
        self.α = states[5]

    @property
    def state(self):

        temp = [self.x,
                self.v,
                self.θ,
                self.ω]
        return temp

    @property
    def extState(self):

        temp = [self.x,
                self.v,
                self.a,
                self.θ,
                self.ω,
                self.α]

        return temp

    @property
    def done(self):
        return abs(self.θ) > (math.pi / 8) or abs(self.x) > cnst.x_threshold

        # @property
        # def reward(self):
        #    #return - self.θ**2
        # return - abs(self.θ)

    #    return - abs(self.θ) - abs(self.x) / 2

    @property
    def reward(self):
        # return - (normalizeAngle(self.θ) ** 2) - (self.x ** 2)
        return - (self.θ ** 2) - (self.x ** 2)


def normalizeAngle(angle):
    angle %= 2 * math.pi
    if angle > math.pi:
        return angle - 2 * math.pi
    return angle
