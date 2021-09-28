import random
import dots
import math
import relationships


class Cluster:

    def __init__(self, canvas):

        self.canvas = canvas
        self.r = random.randint(dots.RADIUS*5, dots.RADIUS*8)

        # center of the circle (x, y)
        self.x = random.randint(dots.BUFFER, dots.WIDTH - dots.BUFFER)
        self.y = random.randint(dots.BUFFER, dots.HEIGHT - dots.BUFFER)

        self.numDots = random.randint(2,6)
        self.dotList = []
        self.color = "#%06x" % random.randint(0, 0xFFFFFF)

        r = self.r * math.sqrt(random.random())
        while len(self.dotList) < self.numDots:
            # random angle
            alpha = 2 * math.pi * random.random()

            # calculating coordinates
            x = r * math.cos(alpha) + self.x
            y = r * math.sin(alpha) + self.y

            d = dots.Dot(self.canvas, x, y, color=self.color)
            if relationships.is_touching(self.canvas, d):
                canvas.delete(d.ovalObject)

            else:
                self.dotList.append(d)

