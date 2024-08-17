import random
import pygame

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (127, 127, 127)

pygame.init()
screen = pygame.display.set_mode((640, 240))
pygame.display.set_caption(f'Lines')

background = GRAY
screen.fill(background)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                screen.fill(background)
            elif event.key == pygame.K_d:
                color = random.choice([RED, GREEN, BLUE, BLACK])
                pygame.draw.line(screen, color, (random.randrange(1, 640), random.randrange(0, 240)),(random.randrange(1, 640), random.randrange(0, 240)))
    pygame.display.update()

pygame.quit()
