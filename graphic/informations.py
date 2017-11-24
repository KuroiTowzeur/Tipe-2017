import pyglet

RAD2DEGRE = 57.2957795131


class Informations:
    def __init__(self, window, states=[0, 0, 0, 0]):
        self.window = window
        self.states = states

        # self.text = 'Hello, world!'
        self.text = self.formatStates(self.states)

        self.x = 100
        self.y = 100

        self.label = pyglet.text.Label(self.text,
                                       batch=self.window.myBatch,
                                       group=window.foreground,
                                       multiline=True,
                                       width=150,
                                       anchor_x='left',
                                       anchor_y='bottom'
                                       )
        self.label.x = 665
        self.label.y = 10

        marge = 10

        ww, wh = self.window.width, self.window.height
        tw, th = self.label.content_width, self.label.content_height

        '''
        anchor = 'bot-rigth'

        if anchor == 'top-rigth':
            self.label.x = ww - tw - marge
            self.label.y = wh - th - marge
        elif anchor == 'top-left':
            self.label.x = marge
            self.label.y = wh - th - marge
        elif anchor == 'bot-rigth':
            self.label.x = ww - tw - 2 * marge
            self.label.y = marge
        elif anchor == 'bot-left':
            self.label.x = marge
            self.label.y = marge
        '''

    def formatStates(self, states):
        output = []

        # output.append('x : {number:.{digits}f} m\n'.format(number=states[0], digits=2))
        # output.append('v : {number:.{digits}f} m.s⁻¹\n'.format(number=states[1], digits=2))

        output.append('x : {} m\n'.format(dsf2(states[0])))
        output.append('v : {} m.s⁻¹\n'.format(dsf2(states[1])))

        unite = 1
        '''
        if unite == 0:
            output.append('θ : {number:.{digits}f} rad\n'.format(number=states[2], digits=2))
            output.append('ω : {number:.{digits}f} rad.s⁻¹'.format(number=states[3], digits=2))'''

        output.append('θ : {number:.{digits}f} °\n'.format(number=RAD2DEGRE * states[2], digits=0))
        output.append('ω : {number:.{digits}f} °.s⁻¹'.format(number=states[3] * states[2], digits=2))

        return ''.join(output)


def dsf(n):
    p = 0

    # print(n)

    if n < 1:
        while 10 ** p > abs(n):
            p -= 1
        return p
    elif n >= 1:
        while 10 ** p < n:
            p += 1
        return p - 1

    else:
        raise ValueError('n pas bon ')


def dsf2(n, nbSignificatif=2):
    powerUtf = {'0': '⁰',
                '1': '¹',
                '2': '²',
                '3': '³',
                '4': '⁴',
                '5': '⁵',
                '6': '⁶',
                '7': '⁷',
                '8': '⁸',
                '9': '⁹',
                '-': '⁻',
                '+': '⁺'}

    if n != 0.0:

        p = dsf(n)

        out = round(n * 10 ** -p, nbSignificatif)
        out2 = str(out)

        final = out2

        if p < -3:
            return '0.00'
        if p == 0:
            return out2
        return final + '.10' + ''.join([powerUtf[pi] for pi in str(p)])
    return '0.00'


if __name__ == '__main__':
    a = 0.0158
    b = 10 ** -2
    c = 587417845
    d = 0

    dsf2(a)
    dsf2(b)
    dsf2(c)
