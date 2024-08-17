import pygame

pygame.init()

GRAY = (127, 127, 127)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

screen = pygame.display.set_mode((600, 300))
backgrounds = {
    pygame.K_r: RED,
    pygame.K_g: GREEN,
    pygame.K_b: BLUE,
    pygame.K_y: YELLOW
}
background = GRAY
pygame.display.set_caption(f'Colors - Current background\'s RGB value: {background}')

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            try:
                background = backgrounds[event.key]
            except KeyError:
                print("Invalid key")
            pygame.display.set_caption(f'Colors - Current background\'s RGB value: {background}')

    # Changing the background color with a string
    # screen.fill('yellow')
    # Changing the background color with RGB values as av tuple
    # screen.fill((125, 125, 0))
    screen.fill(background)

    pygame.display.update()

pygame.quit()
