import pygame
import os

# colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
# colors

# Load graphics
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'imgs')
img_bullet = pygame.image.load(os.path.join(img_folder, 'bullet7.png'))
img_bullet_2 = pygame.image.load(os.path.join(img_folder, 'bullet5.png'))


class bullet_1(pygame.sprite.Sprite):
    def __init__(self, screen, x, y):
        super().__init__()
        self.image = img_bullet
        self.screen = screen
        # self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.speedx = 15
        self.speedy = 10
        self.rect.bottom = y
        self.rect.centerx = x

    def update(self):
        self.rect.x += self.speedx
        # kill if it moves off the top of game's screen
        if self.rect.left < 0 or self.rect.right > self.screen.get_width():
            self.kill()


class bullet_2(pygame.sprite.Sprite):
    def __init__(self, screen, x, y):
        super().__init__()
        self.image = img_bullet_2
        self.image = pygame.transform.scale(img_bullet_2, (70, 50))
        self.screen = screen
        # self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.speedx = -12
        self.speedy = -7
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.speedx -= 5
        self.rect.x += self.speedx
        if self.rect.right < 0 or self.rect.left > self.screen.get_width():
            self.kill()
        if self.rect.top > self.screen.get_height() or self.rect.bottom < 0:
            self.kill()
