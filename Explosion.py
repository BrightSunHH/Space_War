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
explosion_anime = {}
explosion_anime['rocks'] = []
# explosion_anime['player'] = []

# load graphics
for i in range(0, 9):
    filename = 'regularExplosion0{}.png'.format(i)
    img = pygame.image.load(filename)
    img.set_colorkey(black)
    # img_small = pygame.transform.scale(img, (32, 32))
    explosion_anime['rocks'].append(img)


class explosion(pygame.sprite.Sprite):
    def __init__(self, screen, centerx, centery, type):
        pygame.sprite.Sprite.__init__(self)
        self.type = type
        self.screen = screen
        self.image = explosion_anime[self.type][0]
        self.rect = self.image.get_rect()
        self.rect.centerx = centerx
        self.rect.centery = centery
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 9

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(explosion_anime[self.type]):
                self.kill()

            else:
                centerx = self.rect.centerx
                centery = self.rect.centery
                self.image = explosion_anime[self.type][self.frame]
                self.rect = self.image.get_rect()
                self.rect.centerx = centerx
                self.rect.centery = centery
