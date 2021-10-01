import dots
import clusters
import relationships
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
        if p > 0.99: d.jitter_dot()
    canvas.update()


if __name__ == '__main__':
    clusterList = []
    for i in range(2):
        clusterList.append(clusters.Cluster(canvas))

    nestedDots = [c.dotList for c in clusterList]
    allDots = [d for sublist in nestedDots for d in sublist]

    user = self.Self(canvas, root)
    while True:
        jitter_all_dots(canvas, allDots)
        found = False
        for c in clusterList:
            if relationships.is_on_cluster_boundary(canvas, user, c):
                user.set_cluster(c)
                found = True
                break

        if not found:
            user.set_cluster(None)


