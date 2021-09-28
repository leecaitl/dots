import dots
import clusters
import self
import random
import tkinter as tk
import itertools


HEIGHT = 900
WIDTH = 1700

root = tk.Tk()
canvas = tk.Canvas(root, bg="white", height=HEIGHT, width=WIDTH)
canvas.pack()


def jitter_all_dots(canvas, dotList):
    for d in dotList:
        p = random.random()
        if p > 0.9995: d.jitter_dot()
    canvas.update()


if __name__ == '__main__':
    clusterList = []
    for i in range(5):
        clusterList.append(clusters.Cluster(canvas))

    nestedDots = [c.dotList for c in clusterList]
    allDots = [d for sublist in nestedDots for d in sublist]

    user = self.Self(canvas, root)
    while True:
        jitter_all_dots(canvas, allDots)

    root.mainloop()
