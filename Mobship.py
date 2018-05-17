import pygame

# colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
# colors

# Load graphics
img_mobship = pygame.image.load('mobship_1.png')


class mob_ship(pygame.sprite.Sprite):
    def __init__(self, screen):
        super().__init__()
        self.image = pygame.transform.scale(img_mobship, (40, 28))
        self.screen = screen
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width / 3)
        # pygame.draw.circle(self.image, red, self.rect.center, self.radius)
        self.rect.x = self.screen.get_width() + 1000
        self.rect.y = 500
        self.speedx = -10
        self.speedy = -10
        self.full_hp = 100
        self.hp = 100

    def AI_control_outside(self):
        self.rect.x += self.speedx
        self.rect.y += 0

    def AI_control_inside(self):
        # Border control
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.right > self.screen.get_width():
            self.speedx *= -1
        if self.rect.left < self.screen.get_width() / 2:
            self.speedx *= -1
        if self.rect.bottom > self.screen.get_height():
            self.speedy *= -1
        if self.rect.top < 0:
            self.speedy *= -1
