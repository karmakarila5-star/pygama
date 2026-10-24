import pygame
import sys

pygame.init()

win_w = 800
win_h = 600
screen = pygame.display.set_mode((win_w, win_h))

x = 370
y = 280
w = 60
h = 40
speed = 5

my_color = (255, 255, 255)
shape_type = 0

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if shape_type == 0:
                    shape_type = 3
                else:
                    shape_type = 0

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x = x - speed
    if keys[pygame.K_RIGHT]:
        x = x + speed
    if keys[pygame.K_UP]:
        y = y - speed
    if keys[pygame.K_DOWN]:
        y = y + speed

    my_color = (255, 255, 255)

    if x < 0:
        x = 0
        my_color = (255, 0, 0)
    if x > win_w - w:
        x = win_w - w
        my_color = (0, 255, 0)
    if y < 0:
        y = 0
        my_color = (0, 0, 255)
    if y > win_h - h:
        y = win_h - h
        my_color = (255, 255, 0)

    screen.fill((50, 50, 50))
    
    pygame.draw.rect(screen, my_color, (x, y, w, h), shape_type)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()