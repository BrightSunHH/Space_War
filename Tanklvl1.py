import pygame


class tank_1(pygame.sprite.Sprite):
    def __init__(self, screen):
        super().__init__()
        self.image = pygame.image.load('tank1.png')
        self.screen = screen
        self.rect = self.image.get_rect()
        self.speedx = 5
        self.speedy = 5

    def manual_control(self):
        self.rect.x += self.x_move
        self.rect.y += self.y_move
        if self.rect.right > self.screen.get_width() or self.rect.left < 0:
            print('borders collision')
        if self.rect.bottom > self.screen.get_height() or self.rect.top < 0:
            print('borders collision')

    def AI_control(self):

        self.rect.left -= self.speedx
        if self.rect.right > self.screen.get_width() or self.rect.left < 0:
            self.speedx = -self.speedx
