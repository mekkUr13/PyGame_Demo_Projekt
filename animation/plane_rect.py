import pygame

WIDTH, HEIGHT = 800, 400
BG_COLOR = (140, 233, 246)
plane_SPEED = 5

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

plane_surf = pygame.image.load('../img/2_Plane/modified/Fly_2.png').convert_alpha()
plane_rect = plane_surf.get_rect(midleft=(0, HEIGHT / 2))
plane_forward = 1

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BG_COLOR)

    if plane_rect.right <= WIDTH and plane_rect.left >= 0:
        plane_rect.left += plane_SPEED * plane_forward
    else:
        plane_forward *= -1
        plane_surf = pygame.transform.flip(plane_surf, True, False)
        plane_rect = plane_surf.get_rect(midleft=(0, HEIGHT / 2)) if plane_forward > 0 else plane_surf.get_rect(midright=(WIDTH, HEIGHT / 2))

    screen.blit(plane_surf, plane_rect)
    pygame.display.update()
    clock.tick(60)

pygame.quit()
