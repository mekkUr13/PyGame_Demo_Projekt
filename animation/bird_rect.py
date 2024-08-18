import pygame

WIDTH, HEIGHT = 800, 400
BG_COLOR = (140, 233, 246)
BIRD_SPEED = 5

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

bird_surf = pygame.image.load('../img/birds/bird1.png').convert_alpha()
bird_rect = bird_surf.get_rect(midleft=(0, HEIGHT / 2))
bird_forward = 1

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BG_COLOR)

    if bird_rect.right <= WIDTH and bird_rect.left >= 0:
        bird_rect.left += BIRD_SPEED * bird_forward
    else:
        bird_forward *= -1
        bird_surf = pygame.transform.flip(bird_surf, True, False)
        bird_rect = bird_surf.get_rect(midleft=(0, HEIGHT / 2)) if bird_forward > 0 else bird_surf.get_rect(midright=(WIDTH, HEIGHT / 2))

    screen.blit(bird_surf, bird_rect)
    pygame.display.update()
    clock.tick(60)

pygame.quit()
