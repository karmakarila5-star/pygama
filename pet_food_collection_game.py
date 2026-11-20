import pygame
import random

pygame.init()
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pet Food Game")

bg_image = pygame.image.load("background.png")
bg_image = pygame.transform.scale(bg_image, (WIDTH, HEIGHT))

pet = pygame.sprite.Sprite()
pet.image = pygame.image.load("pet.png")
pet.image = pygame.transform.scale(pet.image, (60, 60))
pet.rect = pet.image.get_rect()
pet.rect.center = (WIDTH // 2, HEIGHT // 2)

food_group = pygame.sprite.Group()
food_img = pygame.image.load("food.png")
food_img = pygame.transform.scale(food_img, (35, 35))

for i in range(5):
    food = pygame.sprite.Sprite()
    food.image = food_img
    food.rect = food.image.get_rect()
    food.rect.x = random.randint(50, WIDTH - 50)
    food.rect.y = random.randint(50, HEIGHT - 50)
    food_group.add(food)

my_font = pygame.font.SysFont("Arial", 48)
win_text = my_font.render("All Food Collected!", True, (255, 255, 255))
text_rect = win_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))

clock = pygame.time.Clock()
running = True
speed = 5

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        pet.rect.x -= speed
    if keys[pygame.K_RIGHT]:
        pet.rect.x += speed
    if keys[pygame.K_UP]:
        pet.rect.y -= speed
    if keys[pygame.K_DOWN]:
        pet.rect.y += speed

    if pet.rect.left < 0:
        pet.rect.left = 0
    if pet.rect.right > WIDTH:
        pet.rect.right = WIDTH
    if pet.rect.top < 0:
        pet.rect.top = 0
    if pet.rect.bottom > HEIGHT:
        pet.rect.bottom = HEIGHT

    pygame.sprite.spritecollide(pet, food_group, True)

    screen.blit(bg_image, (0, 0))
    food_group.draw(screen)
    screen.blit(pet.image, pet.rect)

    if len(food_group) == 0:
        screen.blit(win_text, text_rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
