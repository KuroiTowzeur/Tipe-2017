import pyglet
import math


def changeOrigin(pos, u, sign=+1):
    '''en envoie en parametre les (x,y) en pixel par rapport au centre de l'ecran
    et on renvoie en sortie ces coordonnés en fonction de de l'origine de l'ecran'''

    return [pos[0] + sign * u[0],
            pos[1] + sign * u[1]]


class Pole:
    def __init__(self, window, x0=0, θ0=0, longueur=200, largeur=30):
        self.window = window

        # init des parametre liée à la perche
        self.x = x0
        self.θ = θ0 + (math.pi / 2) # dephasage avec le model de simulation

        self.offsetPivot = largeur // 2
        self.longueur = longueur - self.offsetPivot
        self.largeur = largeur

        self.color = (65, 176, 255)

        self.vertex_list = self.window.myBatch.add(4,
                                                   pyglet.gl.GL_QUADS,
                                                   self.window.midground,
                                                   ('v2f/stream', (0, 0) * 4),
                                                   ('c3B/static', self.color * 4)
                                                   )

        self.rotation(0)

    def rotation(self, dangle):
        '''notation :
        indice 0 : repère de l'ecran
        indice 1 : repère liée au x de l'ecran'''

        self.θ += dangle

        # x de lecran dans repere 0
        B0 = (self.window.width // 2 + self.x, self.window.height // 2)

        # partie la plus petite
        V1 = [(math.cos(self.θ + math.pi) * self.offsetPivot),
              (math.sin(self.θ + math.pi) * self.offsetPivot)]
        V1x, V1y = V1

        P1x = (-V1y * (self.largeur // 2) / math.sqrt(V1x ** 2 + V1y ** 2)) + V1x
        P1y = (V1x * (self.largeur // 2) / math.sqrt(V1x ** 2 + V1y ** 2)) + V1y
        P1 = changeOrigin((P1x, P1y), u=B0, sign=+1)

        P2x = (V1y * (self.largeur // 2) / math.sqrt(V1x ** 2 + V1y ** 2)) + V1x
        P2y = (-V1x * (self.largeur // 2) / math.sqrt(V1x ** 2 + V1y ** 2)) + V1y
        P2 = changeOrigin((P2x, P2y), u=B0, sign=+1)

        # partie la plus grande
        U1 = [(math.cos(self.θ) * self.longueur),
              (math.sin(self.θ) * self.longueur)]
        U1x, U1y = U1

        P3x = (-U1y * (self.largeur // 2) / math.sqrt(U1x ** 2 + U1y ** 2)) + U1x
        P3y = (U1x * (self.largeur // 2) / math.sqrt(U1x ** 2 + U1y ** 2)) + U1y
        P3 = changeOrigin((P3x, P3y), u=B0, sign=+1)

        P4x = (U1y * (self.largeur // 2) / math.sqrt(U1x ** 2 + U1y ** 2)) + U1x
        P4y = (-U1x * (self.largeur // 2) / math.sqrt(U1x ** 2 + U1y ** 2)) + U1y
        P4 = changeOrigin((P4x, P4y), u=B0, sign=+1)

        # render de la pole en entière
        self.vertex_list.vertices = (P1 + P2 + P3 + P4)

    def translation(self, dx):
        self.x += dx

        for i in range(0, 8, 2):
            self.vertex_list.vertices[i] += dx

