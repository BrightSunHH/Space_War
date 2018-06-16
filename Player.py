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
img_player = pygame.image.load(os.path.join(img_folder, 'drone_1_blue.png'))


class player_1(pygame.sprite.Sprite):
    def __init__(self, screen):
        super().__init__()
        self.image = pygame.transform.scale(img_player, (50, 38))
        self.screen = screen
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width / 3)
        # pygame.draw.circle(self.image, red, self.rect.center, self.radius)
        self.rect.x = 100
        self.rect.y = 100
        self.speedx = 0
        self.speedy = 0
        self.full_hp = 100
        self.hp = 100
        self.lives = 3
        self.hidden = False
        self.hide_timer = pygame.time.get_ticks()
        self.border_control = True

    def manual_control(self):
        # initial speed set to 0
        self.speedx = 0
        self.speedy = 0

        # controls rules
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -10
        if keystate[pygame.K_RIGHT]:
            self.speedx = 10
        self.rect.x += self.speedx
        if keystate[pygame.K_UP]:
            self.speedy = -10
        if keystate[pygame.K_DOWN]:
            self.speedy = 10
        self.rect.y += self.speedy

        # hide and relocate when death occures

        if self.hidden and pygame.time.get_ticks() - self.hide_timer > 1000:
            self.hidden = False
            self.border_control = True
            self.rect.x = 100
            self.rect.y = 100

        # screen borders rules
        if self.border_control:
            if self.rect.right > self.screen.get_width():
                self.rect.right = self.screen.get_width()
            if self.rect.left < 0:
                self.rect.left = 0
            if self.rect.bottom > self.screen.get_height():
                self.rect.bottom = self.screen.get_height()
            if self.rect.top < 50:
                self.rect.top = 50

    def hide(self):
        self.hidden = True
        self.border_control = False
        self.hide_timer = pygame.time.get_ticks()
        self.rect.x = 2000
        self.rect.y = 1000
