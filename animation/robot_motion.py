import pygame

WIDTH, HEIGHT = 1000, 500
BG_COLOR = (140, 233, 246)
robot_SPEED = 5

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

robot_surf = [pygame.transform.rotozoom(pygame.image.load(f'../img/robot/Run_{i}.png').convert_alpha(),0, 0.5) for i in range(1,9)]
robot_index = 0
robot_rect = robot_surf[robot_index].get_rect(midleft=(0, HEIGHT / 2))
robot_forward = 1
counter = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BG_COLOR)
    counter = (counter + 1) % 3
    robot_index = (robot_index + 1) % len(robot_surf) if counter == 0 else robot_index

    if robot_rect.right <= WIDTH+50 and robot_rect.left >= -50:
        robot_rect.left += robot_SPEED * robot_forward
    else:
        robot_forward *= -1
        robot_surf = [pygame.transform.flip(robot_surf_i, True, False) for robot_surf_i in robot_surf]
        robot_rect = robot_surf[robot_index].get_rect(midleft=(0, HEIGHT / 2)) if robot_forward > 0 else robot_surf[robot_index].get_rect(midright=(WIDTH, HEIGHT / 2))

    screen.blit(robot_surf[robot_index], robot_rect)
    pygame.display.update()
    clock.tick(60)

pygame.quit()
