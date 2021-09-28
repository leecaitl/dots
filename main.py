import dots
import clusters
import self
import random
import tkinter as tk


HEIGHT = 900
WIDTH = 1700

root = tk.Tk()
canvas = tk.Canvas(root, bg="white", height=HEIGHT, width=WIDTH)
canvas.pack()


def move_dots(toMove):
    for i in range(50):
        for d in toMove:
            d.move_dot()
        canvas.update()


if __name__ == '__main__':

    clusterList = []
    for i in range(5):
        clusterList.append(clusters.Cluster(canvas))

    user = self.Self(canvas, root)


    #for i in range(50):
    #    for c in clusterList:
    #        for d in c.dotList:
    #            p = random.random()
    #            if p > 0.90: d.jitter_dot()
    #    canvas.update()

    root.mainloop()
