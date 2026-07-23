import settings
import math
import numpy as np


def NEW_mandelbrot(width, height, xx, yy, scale, max_iterations):
    re = (xx - width / 2) * scale
    im = -(yy - height / 2) * scale
    c = re + (im * 1j)
    z = np.zeros_like(c, dtype=np.complex64)
    iterations = np.zeros(c.shape, dtype= np.float32)
    mask = np.ones(c.shape, dtype=bool)
    for i in range(max_iterations):
        z[mask] = z[mask] * z[mask] + c[mask]
        escaped = np.abs(z) > 2
        newly_escaped = escaped & mask
        iterations[newly_escaped] = (i + 1 - (np.log(np.log(np.abs(z[newly_escaped]))) / np.log(2)))
        mask[newly_escaped] = False
    iterations[mask] = max_iterations
    return iterations




def Julia_fractal(width, height, xx, yy, scale, max_iterations):
    re = (xx - width / 2) * scale
    im = -(yy - height / 2) * scale
    z = re + (im * 1j)
    c = complex(-0.8, 0.156)
    iterations = np.zeros(z.shape, dtype=np.float32)
    mask = np.ones(z.shape, dtype=bool)
    for i in range(max_iterations):
        if not np.any(mask):
            break
        z[mask] = z[mask] * z[mask] + c
        escaped = np.abs(z) > 2
        newly_escaped = escaped & mask
        if np.any(newly_escaped):
            iterations[newly_escaped] = (i - (np.log(np.log(np.abs(z[newly_escaped]))) / np.log(2)))
            mask[newly_escaped] = False
    iterations[mask] = max_iterations
    return iterations
'''def fractal_call(x, y):
    # центрируем действительную ось re
    re = (x - settings.WIDTH / 2) * settings.SCALE
    # центрируем мнимую ось im
    im = (y - settings.HEIGHT / 2) * settings.SCALE
    # задаем комплексное число с
    c = re + (im * 1j)
    # задаем начальное значение z равное нулю
    z = 0
    # задаем переменную для подсчета итераций
    iterations = 0
    # цикл повторяется пока не достигнет максимально допустимого количества итераций
    for _ in range(settings.MAX_ITERATION):
        # задаем формулу фрактала
        z = z*z + c
        # засчитываем итерацию
        iterations += 1
        # сравниваем модуль числа z  с 2
        if abs(z) > 2:
            # если модуль числа z больше чем 2 применяем формулу
            return iterations + 1 - math.log(math.log(abs(z))) /  math.log(2)
        # возвращаем количество итераций
    return iterations'''
