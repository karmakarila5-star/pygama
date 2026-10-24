import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()

LIGHT_EVENT = pygame.USEREVENT + 1

class Car(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 20))
        self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 240
        self.vx = 4

    def update(self):
        self.rect.x += self.vx
        if self.rect.x > 600:
            self.rect.x = -40
            pygame.event.post(pygame.event.Event(LIGHT_EVENT))

class Signal:
    def __init__(self):
        self.colors = [(0, 255, 0), (255, 255, 0), (255, 0, 0)]
        self.idx = 0

    def next_light(self):
        self.idx = (self.idx + 1) % 3

    def draw(self):
        pygame.draw.rect(screen, (50, 50, 50), (280, 80, 40, 100))
        pygame.draw.circle(screen, self.colors[self.idx], (300, 130), 15)

car = Car()
cars = pygame.sprite.Group()
cars.add(car)
traffic = Signal()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == LIGHT_EVENT:
            traffic.next_light()

    cars.update()

    screen.fill((200, 200, 200))
    pygame.draw.rect(screen, (100, 100, 100), (0, 220, 600, 60))
    
    traffic.draw()
    cars.draw(screen)

    pygame.display.flip()
    clock.tick(60)