import pyglet


class Rail:
    def __init__(self, window):
        self.window = window

        point = (0, self.window.height // 2, self.window.width, self.window.height // 2)
        color = (255, 255, 255)

        '''
        self.vertex_list = pyglet.graphics.vertex_list(
            2,
            ('v2i/static', P ),
            ('c3B/static', (0, 0, 0)
        )
        '''

        self.window.myBatch.add(2,
                                pyglet.gl.GL_LINES,
                                self.window.background,
                                ('v2i/static', point),
                                ('c3B/static', color * 2)
                                )

        # def draw(self):
        #   self.vertex_list.draw(pyglet.gl.GL_LINES)
