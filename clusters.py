import random
import dots
import math
import relationships
import time


class Cluster:

    def __init__(self, canvas, dotList=None, x=None, y=None, oldCluster=None, numDots=None):

        self.canvas = canvas

        if oldCluster:
            self.create_from_old_cluster(dotList, oldCluster)
        else:
            if not numDots:
                self.numDots = random.randint(3, 5)
            else:
                self.numDots = numDots

            self.r = random.uniform(dots.RADIUS*self.numDots, dots.RADIUS*(self.numDots+1))

            # center of the circle (x, y)
            if not x:
                self.x = random.randint(dots.BUFFER, dots.WIDTH - dots.BUFFER)
            else:
                self.x = x
            if not y:
                self.y = random.randint(dots.BUFFER, dots.HEIGHT - dots.BUFFER)
            else:
                self.y = y

            self.centerDot = dots.Dot(self.canvas, self.x, self.y, createDot=False)

            # Can't draw the circle for now because then too
            # many intersections
            #self.ovalObject = None
            #self.draw_circle()

            self.color = "#%06x" % random.randint(0, 0xFFFFFF)
            self.dotList = []
            while len(self.dotList) < self.numDots:
                # random angle
                alpha = 2 * math.pi * random.random()

                # calculating coordinates
                x = self.r * math.cos(alpha) + self.x
                y = self.r * math.sin(alpha) + self.y

                d = dots.Dot(self.canvas, x, y, color=self.color, alpha=alpha)
                if relationships.is_touching(self.canvas, d):
                    canvas.delete(d.ovalObject)

                else:
                    self.dotList.append(d)

    def create_from_old_cluster(self, dotList, oldCluster):
        self.numDots = len(dotList)
        self.r = oldCluster.r
        self.x = oldCluster.x
        self.y = oldCluster.y
        self.centerDot = oldCluster.centerDot
        self.color = "#%06x" % random.randint(0, 0xFFFFFF)
        self.dotList = dotList

        for d in self.dotList:
            self.canvas.itemconfig(d.ovalObject, fill=self.color)
        self.canvas.update()

    def draw_circle(self):
        x0 = self.x - self.r
        y0 = self.y - self.r
        x1 = self.x + self.r
        y1 = self.y + self.r

        self.ovalObject = self.canvas.create_oval(x0, y0, x1, y1, outline='black')
        if relationships.is_touching(self.canvas, self):
            self.canvas.delete(self.ovalObject)
            self.x = random.randint(dots.BUFFER, dots.WIDTH - dots.BUFFER)
            self.y = random.randint(dots.BUFFER, dots.HEIGHT - dots.BUFFER)
            self.draw_circle()

    def break_cluster(self):
        if self.numDots < 4:
            return None

        pair = relationships.get_closest_pair(self.dotList)
        newDotList = []
        for i in range(len(pair)):
            newDotList.append(self.dotList[pair[i]])
        newCluster = Cluster(self.canvas, dotList=newDotList, oldCluster=self)

        for i in sorted(pair, reverse=True):
            del self.dotList[i]
        self.numDots = len(self.dotList)

        newCluster.move_cluster()
        newCluster.recenter_cluster()

        self.recenter_cluster()

        return newCluster

    def move_cluster(self, steps=20):
        xSign = 1
        ySign = 1
        if random.random() < 0.5:
            xSign *= -1
        if random.random() < 0.5:
            ySign *= -1

        while relationships.moving_closer_to_center(self.dotList[0], self, xSign, ySign):
            if random.random() < 0.5:
                xSign *= -1
            if random.random() < 0.5:
                ySign *= -1

        for i in range(steps):
            xDir = xSign * random.uniform(0,2)
            yDir = ySign * random.uniform(0,2)

            self.x += xDir
            self.y += yDir

            for d in self.dotList:
                d.x += xDir
                d.y += yDir
                self.canvas.move(d.ovalObject, xDir, yDir)  # move object x, y
                if relationships.out_of_bounds(d) or relationships.is_touching(self.canvas, d):
                    d.x -= xDir
                    d.y -= yDir
                    self.canvas.move(d.ovalObject, -xDir, -yDir)  # move object x,y

                time.sleep(0.2)
                self.canvas.update()
                if i % 4 == 0:
                    d.jitter_dot()

    def close_cluster(self):
        self.r -= 1

        for d in self.dotList:
            ydelt = (self.y - d.y)/abs(self.y - d.y)
            xdelt = (self.x - d.x)/abs(self.x - d.x)

            d.x += xdelt
            d.y += ydelt
            self.canvas.move(d.ovalObject, xdelt, ydelt)  # move object x, y
            if relationships.out_of_bounds(d) or relationships.is_touching(self.canvas, d):
                d.x -= xdelt
                d.y -= ydelt
                self.canvas.move(d.ovalObject, -xdelt, -ydelt)  # move object x,y

    def recenter_cluster(self):
        if self.numDots == 2:
            self.x, self.y = relationships.get_midpoint(self.dotList[0], self.dotList[1])
            self.centerDot = dots.Dot(self.canvas, self.x, self.y, createDot=False)
            self.r = relationships.distance_between(self, self.dotList[0])