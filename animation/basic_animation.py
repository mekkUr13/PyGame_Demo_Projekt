import pygame

WIDTH, HEIGHT = 600, 300
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BG_COLOR = (127, 127, 127)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
rect_pos_x = 0
rect_pos_y = 0
rect_pos_x_2 = WIDTH-100
rect_pos_y_2 = 0

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BG_COLOR)
    rect_pos_x += 6 if rect_pos_x < WIDTH - 100 else 0
    rect_pos_y += 3 if rect_pos_y < HEIGHT - 50 else 0
    rect_pos_x_2 -= 6 if rect_pos_x_2 > 0 else 0
    rect_pos_y_2 += 3 if rect_pos_y_2 < HEIGHT - 50 else 0
    rect = pygame.Rect(rect_pos_x, rect_pos_y, 100, 50)
    rect_2 = pygame.Rect(rect_pos_x_2, rect_pos_y_2, 100, 50)
    pygame.draw.rect(screen, BLUE, rect)
    pygame.draw.rect(screen, GREEN, rect_2)
    pygame.display.update()
    clock.tick(60)

pygame.quit()
