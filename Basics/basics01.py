import pygame

pygame.init()
screen = pygame.display.set_mode((690, 333))
pygame.display.set_caption('Basics')

running = True
while running:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()

pygame.quit()
