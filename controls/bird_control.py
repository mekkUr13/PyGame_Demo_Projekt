import pygame

WIDTH = 1280
HEIGHT = 620
SPEED = 5

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

bird = pygame.image.load('../img/birds/bird1.png').convert_alpha()
bird_x = WIDTH / 2
bird_y = HEIGHT / 2
bird_rect = bird.get_rect(center=(bird_x, bird_y))

forward = True
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and bird_rect.right <= WIDTH:
        bird = pygame.transform.flip(bird, True, False) if not forward else bird
        forward = True
        bird_x += SPEED
    elif keys[pygame.K_LEFT] and bird_rect.left >= 0:
        bird = pygame.transform.flip(bird, True, False) if forward else bird
        forward = False
        bird_x -= SPEED

    if keys[pygame.K_UP] and bird_rect.top >= 0:
        bird_y -= SPEED
    elif keys[pygame.K_DOWN] and bird_rect.bottom <= HEIGHT:
        bird_y += SPEED

    screen.fill((140, 233, 246))
    bird_rect = bird.get_rect(center=(bird_x, bird_y))
    screen.blit(bird, bird_rect)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
