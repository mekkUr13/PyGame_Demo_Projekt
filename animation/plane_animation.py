import pygame
from pygame.transform import rotozoom

WIDTH, HEIGHT = 1200, 600
BG_COLOR = (140, 233, 246)
BIRD_SPEED = 5

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
plane_surf = rotozoom(pygame.image.load('../img/2_Plane/modified/Fly_2.png').convert_alpha(), 0, 3)
background_surf = pygame.image.load('../img/2_Plane/modified/BG.png').convert_alpha()
plane_x = 0
plane_y = 200

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background_surf, (0, 0))
    plane_x += BIRD_SPEED if plane_x < WIDTH else -plane_x
    screen.blit(plane_surf, (plane_x, plane_y))
    pygame.display.update()
    clock.tick(60)

pygame.quit()
