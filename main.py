import pygame
import sys


pygame.init()


def lerp(x1, y1, x2, y2, t):
    return x1 + t * (x2 - x1), y1 + t * (y2 - y1)


def bezier_curves(dots):
    dots0 = []
    dots1 = [*dots]
    dots2 = []

    t = 0.01
    while t <= 1:
        while len(dots1) != 1:
            for i in range(len(dots1) - 1):
                dots2.append(lerp(*dots1[i], *dots1[i + 1], t))
            dots1 = [*dots2]
            dots2 = []
        dots0 += dots1
        dots1 = [*dots]
        dots2 = []
        t += 0.01

    return dots0


fps = 60
window_size = (500, 500)
background_color = (255, 255, 255)
radius = 5

window = pygame.display.set_mode(window_size)
clock = pygame.time.Clock()

dots = []
dots0 = []
clicked = None

while True:

    window.fill(background_color)

    if len(dots) > 2:
        pygame.draw.aalines(window, (0, 255, 0), False, dots)
        pygame.draw.aalines(window, (0, 0, 255), False, dots0)

    for coords in dots:
        pygame.draw.circle(window, (255, 0, 0), coords, radius)

    if not clicked is None:
        dots[i] = pygame.mouse.get_pos()
        dots0 = bezier_curves(dots)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for i in range(len(dots)):
                if (event.pos[0] - dots[i][0]) ** 2 + (event.pos[1] - dots[i][1]) ** 2 <= radius ** 2:
                    clicked = i
                    break
            else:
                dots.append(event.pos)
                dots0 = bezier_curves(dots)

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            for i in range(len(dots)):
                if (event.pos[0] - dots[i][0]) ** 2 + (event.pos[1] - dots[i][1]) ** 2 <= radius ** 2:
                    dots.pop(i)
                    dots0 = bezier_curves(dots)
                    break

        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            clicked = None

    pygame.display.update()
    clock.tick(fps)
