import pygame

# colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
# colors

# Load graphics
img_bullet = pygame.image.load('bullet7.png')
img_bullet_2 = pygame.image.load('bullet5.png')


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
        self.screen = screen
        # self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.speedx = 7
        self.speedy = 7
        self.rect.bottom = y
        self.rect.centerx = x

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        # kill if it moves off the top of game's screen
        if self.rect.left < 0 or self.rect.right > self.screen.get_width():
            self.kill()
        if self.rect.bottom < 0 or self.rect.top > self.screen.get_height():
            self.kill()
