import dots
import relationships
import random


class Self:

    def __init__(self, canvas, root, x=None, y=None, color='#404040'):
        if x is None and y is None:
            x = random.randint(0, dots.WIDTH)
            y = random.randint(0, dots.HEIGHT)

        self.root = root
        self.canvas = canvas
        self.x = x
        self.y = y
        self.r = dots.RADIUS
        self.sight = []
        self.conversation = -1
        self.cluster = None
        self.ovalObject = None  # This is the oval object that is being drawn
        self.color = color
        self.create_dot()

        root.bind('<Right>', self.move_dot_Xpos)
        root.bind('<Left>', self.move_dot_Xneg)
        root.bind('<Down>', self.move_dot_Ypos)
        root.bind('<Up>', self.move_dot_Yneg)

    def set_conversation(self, conversation):
        self.conversation = conversation

    def set_cluster(self, cluster):
        self.cluster = cluster
        if not cluster:
            self.color = '#404040'
            self.canvas.itemconfig(self.ovalObject, fill='#404040')
        else:
            self.color = cluster.color
            self.canvas.itemconfig(self.ovalObject, fill=self.color)
        self.canvas.update()

    def create_dot(self):  # center coordinates, radius
        x0 = self.x - self.r
        y0 = self.y - self.r
        x1 = self.x + self.r
        y1 = self.y + self.r

        self.ovalObject = self.canvas.create_oval(x0, y0, x1, y1, fill=self.color)

    def move_dot_Xpos(self, event):
        self.x += 10
        self.canvas.move(self.ovalObject, 10, 0)  # move object x, y
        if relationships.out_of_bounds(self) or relationships.is_touching(self.canvas, self):
            self.x -= 10
            self.canvas.move(self.ovalObject, -10, 0)  # move object x, y
        self.canvas.update()

    def move_dot_Xneg(self, event):
        self.x -= 10
        self.canvas.move(self.ovalObject, -10, 0)  # move object x, y
        if relationships.out_of_bounds(self) or relationships.is_touching(self.canvas, self):
            self.x += 10
            self.canvas.move(self.ovalObject, 10, 0)  # move object x, y
        self.canvas.update()

    def move_dot_Ypos(self, event):
        self.y += 10
        self.canvas.move(self.ovalObject, 0, 10)  # move object x, y
        if relationships.out_of_bounds(self) or relationships.is_touching(self.canvas, self):
            self.y -= 10
            self.canvas.move(self.ovalObject, 0, -10)  # move object x, y
        self.canvas.update()

    def move_dot_Yneg(self, event):
        self.y -= 10
        self.canvas.move(self.ovalObject, 0, -10)  # move object x, y
        if relationships.out_of_bounds(self) or relationships.is_touching(self.canvas, self):
            self.y += 10
            self.canvas.move(self.ovalObject, 0, 10)  # move object x, y
        self.canvas.update()

    def jitter_dot(self):
        deltx = random.randint(-2, 2)
        delty = random.randint(-2, 2)

        self.canvas.move(self.ovalObject, deltx, delty)  # move object x, y