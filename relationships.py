import numpy as np
import dots
import clusters
import math


def angle_between(dot1, dot2):
    m = (dot2.y - dot1.y)/(dot2.x - dot1.x)
    angle = np.rad2deg(np.arctan(m))

    # The dot with the bigger y value needs to have the smaller angle (positive)
    # If the dots have the same x value, then the one with the bigger x value has the smaller angle (positive)

    if dot1.y == dot2.y:
        if dot1.x < dot2.x:
            return -angle, 180-angle
        else:
            return 180-angle, -angle

    if dot1.y < dot2.y:
        return -angle, 180-angle

    return 180-angle, -angle


def out_of_bounds(dot1):
    if dot1.x <= dots.RADIUS or dot1.x >= dots.WIDTH-dots.RADIUS:
        return True
    if dot1.y <= dots.RADIUS or dot1.y >= dots.HEIGHT-dots.RADIUS:
        return True
    return False


def distance_between(dot1, dot2):
    return math.hypot(dot2.x - dot1.x, dot2.y - dot1.y)


# This returns true if the dot is touching ANY other object in the space
def is_touching(canvas, dot):
    x1,y1,x2,y2 = canvas.bbox(dot.ovalObject)
    if len(canvas.find_overlapping(x1, y1, x2, y2)) > 1:
        return True
    return False


def is_on_cluster_boundary(canvas, dot, cluster):
    margin = 3
    center = dots.Dot(canvas, x=cluster.x, y=cluster.y, createDot=False)
    d = distance_between(dot, center)

    if cluster.r - margin <= d <= cluster.r + margin:
        return True

    return False
