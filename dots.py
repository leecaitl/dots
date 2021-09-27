import random
import tkinter as tk

RADIUS = 15
SIGHT_LENGTH = 60
SIGHT_WIDTH = 40  # this is an angle in degrees
TURN_RATE = 5  # the num of degrees per second to turn


class Dot:

    def __init__(self, c, x=None, y=None):
        if x is None and y is None:
            x = random.randint(0, 250)
            y = random.randint(0, 250)

        self.canvas = c
        self.x = x
        self.y = y
        self.r = RADIUS
        self.startAngle = random.randint(0,360)
        self.sight = []
        self.conversation = -1
        self.ovalObject = None  # This is the oval object that is being drawn

        self.sightCoords = [self.x - SIGHT_LENGTH, self.y - SIGHT_LENGTH, self.x + SIGHT_LENGTH, self.y + SIGHT_LENGTH]  # this is going to be the same regardless of the angle
        self.sightObject = None  # This is the sight object that is being drawn

    def set_conversation(self, conversation):
        self.conversation = conversation

    def create_dot(self):  # center coordinates, radius
        x0 = self.x - self.r
        y0 = self.y - self.r
        x1 = self.x + self.r
        y1 = self.y + self.r

        self.sightObject = self.canvas.create_arc(self.sightCoords[0],
                                                  self.sightCoords[1],
                                                  self.sightCoords[2],
                                                  self.sightCoords[3],
                                                  start=self.startAngle, extent=SIGHT_WIDTH, style=tk.PIESLICE,
                                                  fill='#DE9898')

        self.ovalObject = self.canvas.create_oval(x0, y0, x1, y1, fill='#404040')

    def set_sight(self, startAngle=None):
        if startAngle:
            self.startAngle = startAngle

    def draw_dot(self):
        self.set_sight()
        self.create_dot()

    def move_dot(self):
        self.canvas.move(self.ovalObject, 5, 0)  # move object x, y
        self.canvas.update()

    def rotate_sight(self, destAngle):
        destAngle -= SIGHT_WIDTH/2
        if destAngle < 0: destAngle += 360
        if self.startAngle < 0: self.startAngle += 360

        print("dest" + str(destAngle))
        print("start" + str(self.startAngle))

        shortestDist = min(destAngle - self.startAngle, 360 - destAngle + self.startAngle)
        print(shortestDist)

        direction = 1
        if self.startAngle + shortestDist != destAngle: direction = -1
        shortestDist *= direction

        steps = 50
        stepSize = shortestDist/steps

        for i in range(steps):
            self.startAngle += stepSize
            self.canvas.itemconfigure(self.sightObject, start=self.startAngle)
            self.canvas.update()