import pyglet
from math import pi, sin, cos


class Axle:
    def __init__(self, window, x0=0, radius=10):
        self.window = window

        self.radius = radius

        self.x = (self.window.width // 2)
        self.y = (self.window.height // 2)

        self.color = (255, 179, 65)

        self.makeCircleVertice()

        self.vertex_list = self.window.myBatch.add(self.nbPoints,
                                                   pyglet.gl.GL_TRIANGLE_FAN,
                                                   self.window.foreground,
                                                   ('v2f\stream', self.v0),
                                                   ('c3B\static', self.color * self.nbPoints)
                                                   )

    def resetPosition(self):
        self.vertex_list.vertices = self.v0

    def makeCircleVertice(self):

        iterations = round(2 * pi * self.radius)

        s = sin(2 * pi / iterations)
        c = cos(2 * pi / iterations)

        dx, dy = self.radius, 0

        self.v0 = [self.x, self.y]

        for i in range(iterations + 1):
            self.v0.extend([self.x + dx, self.y + dy])
            dx, dy = (dx * c - dy * s), (dy * c + dx * s)

        self.nbPoints = iterations + 2


    def translation(self, dx):

        for i in range(0, self.nbPoints * 2, 2):
            self.vertex_list.vertices[i] += dx
