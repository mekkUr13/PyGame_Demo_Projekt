import pygame


def draw(scr, bg):
    screen.fill(bg)
    pygame.draw.rect(scr, BLUE, (10, 20, 100, 50))
    # rect = Rect(10, 20, 100, 50)
    # pygame.draw.rect(screen, BLUE, rect)
    pygame.draw.rect(scr, BLUE, (120, 20, 100, 50), 5, 10)
    pygame.draw.ellipse(scr, RED, (10, 90, 100, 50))
    pygame.draw.polygon(scr, GREEN, [(120, 90), (120, 190), (200, 150)])
    pygame.draw.circle(scr, BLACK, (300, 100), 20)


BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (127, 127, 127)

pygame.init()
screen = pygame.display.set_mode((640, 240))
pygame.display.set_caption(f'Shapes')

background = GRAY
draw(screen, background)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                screen.fill(background)
            elif event.key == pygame.K_d:
                draw(screen, background)
    pygame.display.update()

pygame.quit()
