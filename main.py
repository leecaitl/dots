import clusters
import relationships
import scenarios
import self
import random
import tkinter as tk


HEIGHT = 900
WIDTH = 1700

root = tk.Tk()
canvas = tk.Canvas(root, bg="white", height=HEIGHT, width=WIDTH)
canvas.pack()


def jitter_all_dots(c, dotList):
    for d in dotList:
        if random.random() > 0.99:
            d.jitter_dot()
    c.update()


def create_clusters_from_scenarios(scenario):
    clusterList = []
    for c in scenario:
        clusterList.append(clusters.Cluster(canvas, x=c[0], y=c[1], numDots=c[2]))

    return clusterList


def create_random_scenario(numClusters):
    clusterList = []
    for i in range(numClusters):
        clusterList.append(clusters.Cluster(canvas))

    return clusterList


if __name__ == '__main__':
    # clusterList = create_random_scenario(2)
    clusterList = create_clusters_from_scenarios(scenarios.SCENARIO1)

    nestedDots = [c.dotList for c in clusterList]
    allDots = [d for sublist in nestedDots for d in sublist]

    user = self.Self(canvas, root, x=WIDTH/2, y=HEIGHT/2)
    while True:
        # always moving the dots around
        jitter_all_dots(canvas, allDots)

        # always checking to see if the user is in any given cluster
        found = False
        for c in clusterList:
            if relationships.is_on_cluster_boundary(canvas, user, c):
                user.set_cluster(c)
                found = True
                break
        if not found:
            user.set_cluster(None)

        # for every cluster, consider breaking it up and also closing it
        for c in clusterList:
            if random.random() > 0.999:
                print('trying to split cluster')
                newCluster = c.break_cluster()
                if newCluster:
                    print('split cluster')
                    clusterList.append(newCluster)
                c.close_cluster()

            if c.r > c.dotList[0].r * 2 and random.random() > 0.999:
                print('closing cluster')
                c.close_cluster()

            if random.random() > 0.999:
                print('moving cluster')
                c.move_cluster()
