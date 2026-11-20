import pygame
import random

pygame.init()

w, h = 640, 480
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("Catch Game")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

player = pygame.Rect(300, 220, 35, 35)
speed = 5
score = 0

enemies = []
for i in range(7):
    ex = random.randint(0, w - 25)
    ey = random.randint(0, h - 25)
    enemies.append(pygame.Rect(ex, ey, 25, 25))

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.x > 0:
        player.x -= speed
    if keys[pygame.K_RIGHT] and player.x < w - player.width:
        player.x += speed
    if keys[pygame.K_UP] and player.y > 0:
        player.y -= speed
    if keys[pygame.K_DOWN] and player.y < h - player.height:
        player.y += speed

    for e in enemies:
        if player.colliderect(e):
            score += 1
            e.x = random.randint(0, w - e.width)
            e.y = random.randint(0, h - e.height)

    screen.fill((25, 25, 35))
    pygame.draw.rect(screen, (50, 200, 100), player)

    for e in enemies:
        pygame.draw.rect(screen, (220, 60, 60), e)

    txt = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(txt, (15, 15))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
