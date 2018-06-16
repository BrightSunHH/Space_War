import pygame
import os

# colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
# colors

# Load graphics
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'imgs')
img_mobship = pygame.image.load(os.path.join(img_folder, 'one_eye.png'))


class mob_ship(pygame.sprite.Sprite):
    def __init__(self, screen):
        super().__init__()
        self.image = pygame.transform.scale(img_mobship, (200, 150))
        self.screen = screen
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width / 3)
        # pygame.draw.circle(self.image, red, self.rect.center, self.radius)
        self.rect.x = self.screen.get_width() + 900
        self.rect.y = 200
        self.speedx = -5
        self.speedy = -10
        self.full_hp = 2000
        self.hp = 2000

    def AI_control_outside(self):
        self.rect.x += self.speedx
        self.rect.y += 0

    def AI_control_inside(self):
        # Border control
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.right > self.screen.get_width():
            self.speedx = -1
        if self.rect.left < self.screen.get_width() / 2 + 200:
            self.speedx = 0
        if self.rect.bottom > self.screen.get_height():
            self.speedy *= -1
        if self.rect.top < 0:
            self.speedy *= -1
