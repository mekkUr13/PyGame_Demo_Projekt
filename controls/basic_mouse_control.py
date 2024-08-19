import pygame
import random
from controls.simple_collision import is_out

WIDTH = 1280
HEIGHT = 620
BALLOON_SPEED = 0.69
GREEN = (0, 200, 0)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

balloon_surf = pygame.image.load('../img/balloon.png').convert_alpha()
balloon_rects = [balloon_surf.get_rect(center=(random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50))) for _ in range(5)]

crosshair_surf = pygame.image.load('../img/crosshair.png').convert_alpha()
crosshair_rect = crosshair_surf.get_rect(center=(WIDTH / 2, HEIGHT / 2))

score_font = pygame.font.SysFont('centaur', 33)

score = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEMOTION:
            crosshair_rect = crosshair_surf.get_rect(center=event.pos)
        if event.type == pygame.MOUSEBUTTONDOWN:
            for index, balloon_rect in enumerate(balloon_rects):
                if balloon_rect.collidepoint(event.pos):
                    del balloon_rects[index]
                    score += 1

    screen.fill((140, 233, 246))

    for index, balloon_rect in enumerate(balloon_rects):
        balloon_rects[index] = balloon_surf.get_rect(center=(balloon_rect.centerx, balloon_rect.centery - BALLOON_SPEED))
        if is_out(balloon_rects[index]):
            del balloon_rects[index]
        else:
            screen.blit(balloon_surf, balloon_rect)

    screen.blit(crosshair_surf, crosshair_rect)

    score_surf = score_font.render('SCORE: ' + str(score), True, GREEN)
    score_rect = score_surf.get_rect(topleft=(10, 10))
    screen.blit(score_surf, score_rect)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
