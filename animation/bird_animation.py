import pygame

WIDTH, HEIGHT = 800, 400
BG_COLOR = (140, 137, 246)
BIRD_SPEED = 5

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
bird_surf = pygame.image.load('../img/bird1.png').convert_alpha()
bird_x = 0
bird_y = 200

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BG_COLOR)
    bird_x += BIRD_SPEED if BIRD_SPEED + bird_x + bird_surf.get_width() < WIDTH else 0
    screen.blit(bird_surf, (bird_x, bird_y))
    pygame.display.update()
    clock.tick(60)

pygame.quit()
