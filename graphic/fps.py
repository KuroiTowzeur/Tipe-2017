import pyglet


class Fps(pyglet.window.FPSDisplay):
    def __init__(self, window, rate=1):
        self.window = window

        super(Fps, self).__init__(self.window)

        pyglet.font.add_file('graphic/static/font/Square.ttf')

        # '%(fps).0f'
        self.label = pyglet.text.Label(text='00',
                                       font_name='SquareFont',
                                       font_size=22,
                                       color=(255, 255, 0, 255),
                                       x=800 - 45, y=600 - 35,
                                       batch=self.window.myBatch,
                                       group=self.window.foreground)

        self.update_period = rate

    def set_fps(self, fps):
        self.label.text = '%.0f' % fps
