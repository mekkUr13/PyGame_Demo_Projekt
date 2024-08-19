import random
import pygame

WIDTH = 1280
HEIGHT = 620
SPEED = 5

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

bird_x = WIDTH / 2
bird_y = HEIGHT / 2
bird_index = 0
birds = [pygame.image.load(f'../img/birds/bird{i}.png').convert_alpha() for i in range(1, 5)]
bird_rect = birds[bird_index].get_rect(center=(bird_x, bird_y))
cloud = pygame.transform.rotozoom(pygame.image.load(f'../img/birds/cloud.png').convert_alpha(), 0, 5)
cloud_x = random.randint(cloud.get_width(), WIDTH-cloud.get_width())
cloud_y = random.randint(cloud.get_height(), min(cloud.get_height()+int(HEIGHT * 0.10), HEIGHT-cloud.get_height()))
cloud_rect = cloud.get_rect(center=(cloud_x, cloud_y))

counter = 0
cloud_forward = True
bird_forward = True
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and bird_rect.right <= WIDTH:
        birds = [pygame.transform.flip(bird, True, False) for bird in birds] if not bird_forward else birds
        bird_forward = True
        bird_x += SPEED
    elif (keys[pygame.K_LEFT] or keys[pygame.K_a]) and bird_rect.left >= 0:
        birds = [pygame.transform.flip(bird, True, False) for bird in birds] if bird_forward else birds
        bird_forward = False
        bird_x -= SPEED

    if (keys[pygame.K_UP] or keys[pygame.K_w]) and bird_rect.top >= 0:
        bird_y -= SPEED
    elif (keys[pygame.K_DOWN] or keys[pygame.K_s]) and bird_rect.bottom <= HEIGHT:
        bird_y += SPEED

    cloud_forward = False if cloud_rect.right >= WIDTH else cloud_forward
    cloud_forward = True if cloud_rect.left <= 0 else cloud_forward
    cloud_x += 2 if cloud_forward else -2

    screen.fill((140, 233, 246))

    counter = (counter + 1) % 7
    bird_index = (bird_index + 1) % len(birds) if counter == 0 else bird_index

    bird_rect = birds[bird_index].get_rect(center=(bird_x, bird_y))
    screen.blit(birds[bird_index], bird_rect)

    cloud_rect = cloud.get_rect(center=(cloud_x, cloud_y))
    screen.blit(cloud, cloud_rect)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
