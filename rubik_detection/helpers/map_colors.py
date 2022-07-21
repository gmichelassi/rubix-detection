import cv2
import numpy as np


def map_colors(r: int, g: int, b: int) -> str:
    if is_white(r, g, b):
        return 'white'

    color = np.uint8([[[b, g, r]]])
    hsv_color = cv2.cvtColor(color, cv2.COLOR_BGR2HSV)
    hue = hsv_color[0][0][0]

    if hue < 10 or hue > 165:
        return 'red'
    elif 10 <= hue < 20:
        return 'orange'
    elif 20 <= hue < 45:
        return 'yellow'
    elif 45 <= hue < 80:
        return 'green'
    elif 80 <= hue < 125:
        return 'blue'

    return 'white'


def is_white(r: int, g: int, b: int) -> bool:
    return r > 125 and g > 125 and b > 125
