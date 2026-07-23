import fractal_calling
import pygame
import settings as set
import numpy as np
import palette




def fractal_render():
    x = np.arange(set.WIDTH)
    y = np.arange(set.HEIGHT)
    xx, yy = np.meshgrid(x,y)
    iterations = fractal_calling.Julia_fractal(set.WIDTH, set.HEIGHT, xx, yy, set.SCALE, set.MAX_ITERATION)
    escaped_nums_mask = abs(iterations) < set.MAX_ITERATION
    paint = palette.paint_in_color(iterations)
    not_esc_mask = iterations == set.MAX_ITERATION
    paint[not_esc_mask] = (0, 0, 0)
    return paint

'''def rendering_fractal(surface):
    #цикл проходится по координатам оси x
    for x in range(settings.WIDTH):
        # цикл проходится по координатам оси y
        for y in range(settings.HEIGHT):
            # подсчет количество итераций на данной координате
            iterations = fractal_calling.fractal_call(x, y)
            # если количество итераций превышает допустимое количество закрашиваем цветом данную координату
            if iterations < settings.MAX_ITERATION:
                surface.set_at((x, y), (palette.CYAN(iterations)))
            # если количество итераций находится в пределах допустимого закрашиваем черным данную координату
            else:
                surface.set_at((x, y), settings.BLACK)'''

