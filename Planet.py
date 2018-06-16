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
# Load graphics
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'imgs')
img_planet = pygame.image.load(os.path.join(img_folder, 'Planet2.png'))


class planet_1(pygame.sprite.Sprite):
    def __init__(self, screen):
        super().__init__()
        self.image = img_planet
        # self.image = pygame.transform.scale(img_planet, (200, 200))
        self.screen = screen
        self.rect = self.image.get_rect()
        self.rect.x = 700
        self.rect.y = -200
        self.speedx = 0
        self.speedy = 0
        self.hidden = False
        self.hide_timer = pygame.time.get_ticks()
        self.border_control = True

    def AI_control(self, score, count):
        self.speedx = -0.5
        shift = (score >= 30) or (count >= 3)
        if shift:
            self.rect.x += self.speedx
            shift = True
            print('shift')
        return shift
