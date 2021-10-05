import random
import relationships
import tkinter as tk

RADIUS = 9
HEIGHT = 900
WIDTH = 1700
BUFFER = RADIUS * 8


class Dot:

    def __init__(self, canvas, x=None, y=None, color='#404040', alpha=-1, createDot=True):
        if x is None and y is None:
            x = random.randint(0, WIDTH-BUFFER)
            y = random.randint(0, HEIGHT-BUFFER)

        self.canvas = canvas
        self.x = x
        self.y = y
        self.r = RADIUS
        self.sight = []
        self.conversation = -1
        self.ovalObject = None  # This is the oval object that is being drawn
        self.color = color
        self.alpha = alpha
        if createDot: self.create_dot()

    def set_conversation(self, conversation):
        self.conversation = conversation

    def create_dot(self):  # center coordinates, radius
        x0 = self.x - self.r
        y0 = self.y - self.r
        x1 = self.x + self.r
        y1 = self.y + self.r

        self.ovalObject = self.canvas.create_oval(x0, y0, x1, y1, fill=self.color)

    def jitter_dot(self):
        deltx = random.randint(-2, 2)
        delty = random.randint(-2, 2)
        self.canvas.move(self.ovalObject, deltx, delty)  # move object x, y

        if relationships.out_of_bounds(self) or relationships.is_touching(self.canvas, self):
            self.x -= deltx
            self.y -= delty
            self.canvas.move(self.ovalObject, -deltx, -delty)  # move object x, y

    def update_coords(self, x, y):
        self.x = x
        self.y = y