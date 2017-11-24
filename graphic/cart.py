import pyglet


class Cart:
    def __init__(self, window, x0=0, longueur=110, largeur=80):
        self.window = window

        self.longueur = longueur
        self.largeur = largeur


        self.x0 = x0
        self.x = x0  # la position initiale % repere normal

        self.v0 = ((self.window.width - self.longueur) // 2 + self.x,
                   (self.window.height - self.largeur) // 2,
                   (self.window.width - self.longueur) // 2 + self.x,
                   (self.window.height + self.largeur) // 2,
                   (self.window.width + self.longueur) // 2 + self.x,
                   (self.window.height + self.largeur) // 2,
                   (self.window.width + self.longueur) // 2 + self.x,
                   (self.window.height - self.largeur) // 2)

        self.color = (26, 52, 201)

        self.vertex_list = self.window.myBatch.add(4,
                                                   pyglet.gl.GL_QUADS,
                                                   self.window.midground,
                                                   ('v2f/stream', self.v0),
                                                   ('c3B/static', self.color * 4))

    def resetPositon(self):
        self.x = self.x0
        self.vertex_list.vertices = self.v0

    def translation(self, dx):
        self.x += dx
        for i in range(0, 8, 2):
            self.vertex_list.vertices[i] += dx
