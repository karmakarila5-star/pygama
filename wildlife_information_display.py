import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Wildlife Display")

back_img = pygame.image.load("background.jpg")
back_img = pygame.transform.scale(back_img, (800, 600))

animal_img = pygame.image.load("wildlife.png")
animal_img = pygame.transform.scale(animal_img, (300, 300))

my_font = pygame.font.SysFont("arial", 40)
text_surface = my_font.render("Nature World", True, (255, 255, 255))

clock = pygame.track = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(back_img, (0, 0))
    screen.blit(animal_img, (250, 200))
    screen.blit(text_surface, (300, 50))

    pygame.display.update()
    clock.tick(60)