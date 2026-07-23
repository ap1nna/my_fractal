import numpy as np
import pygame
import settings
import render
import time
pygame.init()


screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
surface = pygame.Surface((settings.WIDTH, settings.HEIGHT))

clock = pygame.time.Clock()
start = time.perf_counter()
mandelbrot = render.fractal_render()
mandelbrot = np.swapaxes(mandelbrot, axis1=False, axis2=True)
mandelbrot_surface = pygame.surfarray.make_surface(mandelbrot)
print(mandelbrot.shape)
end = time.perf_counter()

print(f"execution time: {end - start:.2f}")

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #screen.fill((255, 255, 255))
    screen.blit(mandelbrot_surface, (0, 0))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()