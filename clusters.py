import random
import dots
import math
import relationships


class Cluster:

    def __init__(self, canvas):

        self.canvas = canvas
        self.r = random.randint(dots.RADIUS*4, dots.RADIUS*6)

        # center of the circle (x, y)
        self.x = random.randint(dots.BUFFER, dots.WIDTH - dots.BUFFER)
        self.y = random.randint(dots.BUFFER, dots.HEIGHT - dots.BUFFER)

        self.ovalObject = None
        #self.draw_circle()

        self.numDots = random.randint(2,6)
        self.dotList = []
        self.color = "#%06x" % random.randint(0, 0xFFFFFF)

        while len(self.dotList) < self.numDots:
            # random angle
            alpha = 2 * math.pi * random.random()

            # calculating coordinates
            x = self.r * math.cos(alpha) + self.x
            y = self.r * math.sin(alpha) + self.y

            d = dots.Dot(self.canvas, x, y, color=self.color)
            if relationships.is_touching(self.canvas, d):
                canvas.delete(d.ovalObject)

            else:
                self.dotList.append(d)

    def draw_circle(self):
        print('here')
        x0 = self.x - self.r
        y0 = self.y - self.r
        x1 = self.x + self.r
        y1 = self.y + self.r

        self.ovalObject = self.canvas.create_oval(x0, y0, x1, y1, outline='black')
        if relationships.is_touching(self.canvas, self):
            print ("stuck")
            self.canvas.delete(self.ovalObject)
            self.x = random.randint(dots.BUFFER, dots.WIDTH - dots.BUFFER)
            self.y = random.randint(dots.BUFFER, dots.HEIGHT - dots.BUFFER)
            self.draw_circle()