import pygame
import sys
from pygame.locals import *

pygame.init()
vec = pygame.math.Vector2  # 2 for two dimensional

HEIGHT = 480
WIDTH = 640
ACC = 0.5
FRIC = -0.12
FPS = 60

FramePerSec = pygame.time.Clock()

displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Peasant Platformer")

bg = pygame.image.load("bg1.png")


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("p1Sprite.png")
        self.rect = self.image.get_rect()
        self.rect.x = 40
        self.rect.y = 400

    def move(self, key):
        if key == 'left':
            if self.rect.x <= 5:
                self.rect.x -= self.rect.x
            else:
                self.rect.x -= 5
        if key == 'right':
            if self.rect.x >= 600:
                self.rect.x = 600
            else:
                self.rect.x += 5

        if key == 'up':
            self.rect.y -= 5


P1 = Player()


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    displaysurface.blit(bg, (0, 0))
    displaysurface.blit(P1.image, P1.rect)

    events = pygame.event.get()
    keys = pygame.key.get_pressed()
    if keys[K_LEFT]:
        P1.move("left")
    if keys[K_RIGHT]:
        P1.move("right")
    if keys[K_UP]:
        P1.move("up")

    pygame.display.update()
    FramePerSec.tick(FPS)
