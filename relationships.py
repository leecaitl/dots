import numpy as np


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
