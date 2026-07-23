import settings
import numpy as np
def paint_in_color(iterations):
    normalized = iterations / settings.MAX_ITERATION
    r = (20 * (1 - normalized) * normalized * 255)
    g = (12 * (1 - normalized) * normalized * 255)
    b = (8.5 * (1 - normalized) * normalized * 255)
    return np.stack([r, g, b], axis=-1).astype(np.uint8)



'''def RED(iterations):
    return iterations * 10 % 255, 0, 0
def BLUE(iterations):
    return 0, 0, iterations * 10 % 255
def GREEN(iterations):
    return 0, iterations * 10 % 255, 0
def PINK(iterations):
    return iterations * 10 % 255, 0, iterations * 5 % 255
def PURPLE(iterations):
    return iterations * 10 % 255, 0, iterations * 10 % 255
def CYAN(iterations):
    return 0, iterations * 10 % 255, iterations * 10 % 255
def RAINBOW(iterations):
    return iterations * 10 % 255, iterations * 12 % 255, iterations * 14 % 255'''
