import numpy as np
import dots
import random
import itertools
import math


def angle_between(dot1, dot2):
    m = (dot2.y - dot1.y) / (dot2.x - dot1.x)
    angle = np.rad2deg(np.arctan(m))

    # The dot with the bigger y value needs to have the smaller angle (positive)
    # If the dots have the same x value, then the one with the bigger x value has the smaller angle (positive)

    if dot1.y == dot2.y:
        if dot1.x < dot2.x:
            return -angle, 180 - angle
        else:
            return 180 - angle, -angle

    if dot1.y < dot2.y:
        return -angle, 180 - angle

    return 180 - angle, -angle


def out_of_bounds(dot1):
    if dot1.x <= dots.RADIUS or dot1.x >= dots.WIDTH - dots.RADIUS:
        return True
    if dot1.y <= dots.RADIUS or dot1.y >= dots.HEIGHT - dots.RADIUS:
        return True
    return False


def distance_between(dot1, dot2):
    return math.hypot(dot2.x - dot1.x, dot2.y - dot1.y)


def get_slope_between(dot1, dot2):
    return (dot2.y - dot1.y) / (dot2.x - dot1.x)


# Getting average distance, pairwise, of dots in cluster
def avg_cluster_distance(cluster):
    pairs = list(itertools.combinations(cluster.dotList, 2))
    distances = []
    for pair in pairs:
        distances.append(distance_between(pair[0], pair[1]))

    return np.mean(distances)


# This returns true if the dot is touching ANY other object in the space
def is_touching(canvas, dot):
    x1, y1, x2, y2 = canvas.bbox(dot.ovalObject)
    if len(canvas.find_overlapping(x1, y1, x2, y2)) > 1:
        return True
    return False


def is_on_cluster_boundary(canvas, dot, cluster):
    margin = dot.r / 2
    center = dots.Dot(canvas, x=cluster.x, y=cluster.y, createDot=False)
    d = distance_between(dot, center)

    if cluster.r - margin <= d <= cluster.r + margin:
        return True

    return False


def is_within_cluster(dot, cluster):
    d = distance_between(cluster.centerDot, dot)
    if d <= cluster.r:
        return True
    return False


def get_closest_pair(dotList):
    oldList = []
    for i in range(len(dotList)):
        oldList.append((i, dotList[i]))

    sortedList = sorted(oldList, key=lambda dotTuple: dotTuple[1].alpha)
    sortedList.append(sortedList[0])

    smallestGap = 10000
    currPair = ()
    for i in range(len(sortedList) - 1):
        if i == len(sortedList) - 2:
            currGap = 2 * math.pi - sortedList[i][1].alpha + sortedList[i + 1][1].alpha
        else:
            currGap = sortedList[i + 1][1].alpha - sortedList[i][1].alpha

        if currGap <= smallestGap:
            smallestGap = currGap
            currPair = (sortedList[i][0], sortedList[i + 1][0])

    return currPair


def get_midpoint(dot1, dot2):
    return (dot1.x + dot2.x) / 2, (dot1.y + dot2.y) / 2


def pick_random_dir():
    directions = [-1,0,1]
    return random.choice(directions), random.choice(directions)


def pick_dir_away_from(toMove, refPoint):
    d = distance_between(toMove, refPoint)

    directions = [-1, 0, 1]
    xDir, yDir = random.choice(directions), random.choice(directions)

    newX = toMove.x + xDir
    newY = toMove.y + yDir

    while math.hypot(newX - refPoint.x, newY - refPoint.y) <= d:
        xDir, yDir = random.choice(directions), random.choice(directions)

        newX = toMove.x + xDir
        newY = toMove.y + yDir

    return xDir, yDir


def cluster_spread_too_far(cluster):
    if cluster.numDots == 2:
        if distance_between(cluster.dotList[0], cluster.dotList[1]) > 2*cluster.r + dots.RADIUS:
            return True
    return False


def intersecting_clusters(c1, c2):
    return
