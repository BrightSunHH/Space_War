import random
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
rocks_small = []
rocks_medium = []
rocks_large = []
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'imgs')
for i in range(1, 13):
    filename = 'rock{}.png'.format(i)
    img = pygame.image.load(os.path.join(img_folder, filename))
    # img.set_colorkey(black)
    # img_small = pygame.transform.scale(img, (32, 32))
    rocks_small.append(img)
for i in range(13, 19):
    filename = 'rock{}.png'.format(i)
    img = pygame.image.load(os.path.join(img_folder, filename))
    # img.set_colorkey(black)
    # img_small = pygame.transform.scale(img, (32, 32))
    rocks_medium.append(img)
for i in range(19, 21):
    filename = 'rock{}.png'.format(i)
    img = pygame.image.load(os.path.join(img_folder, filename))
    # img.set_colorkey(black)
    # img_small = pygame.transform.scale(img, (32, 32))
    rocks_large.append(img)


class space_rock1(pygame.sprite.Sprite):
    def __init__(self, screen, y):
        super().__init__()
        self.screen = screen
        random_number = random.randrange(1, 12)
        self.image_orig = rocks_small[random_number]
        self.image = rocks_small[random_number]
        # self.image_orig = pygame.transform.scale(rocks_set[random_number], (random.randrange(15, 60), random.randrange(25, 80)))
        # self.image = pygame.transform.scale(rocks_set[random_number], (random.randrange(15, 60), random.randrange(25, 80)))
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width / 4)
        # pygame.draw.circle(self.image, red, self.rect.center, self.radius)
        self.speedx = random.randrange(-7, -2)
        # self.speedx = -4
        self.hit_damage = 50
        self.rect.x = self.screen.get_width() + 100
        self.rect.y = y
        # rotation
        self.rot = 0
        self.rot_speed = 1
        self.last_update = pygame.time.get_ticks()

    def rotation(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > 50:
            self.last_update = now
            self.rot = (self.rot + self.rot_speed) % 360
            new_image = pygame.transform.rotate(self.image_orig, self.rot)
            old_center = self.rect.center
            self.image = new_image
            self.rock = self.image.get_rect()
            self.rect.center = old_center

    def AI_control(self):
        # rotation
        self.rotation()
        # controls
        self.rect.x += self.speedx


class space_rock2(pygame.sprite.Sprite):
    def __init__(self, screen, y):
        super().__init__()
        self.screen = screen
        random_number = random.randint(0, 5)
        self.image_orig = rocks_medium[random_number]
        self.image = rocks_medium[random_number]
        # self.image_orig = pygame.transform.scale(rocks_set[random_number], (random.randrange(15, 60), random.randrange(25, 80)))
        # self.image = pygame.transform.scale(rocks_set[random_number], (random.randrange(15, 60), random.randrange(25, 80)))
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width / 3)
        # pygame.draw.circle(self.image, red, self.rect.center, self.radius)
        # self.speedx = -4
        self.speedx = random.randrange(-7, -2)
        self.hit_damage = 50
        self.rect.x = self.screen.get_width() + 100 # random.randint(0, 400)
        self.rect.y = y
        # rotation
        self.rot = 0
        self.rot_speed = 1
        self.last_update = pygame.time.get_ticks()

    def rotation(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > 50:
            self.last_update = now
            self.rot = (self.rot + self.rot_speed) % 360
            new_image = pygame.transform.rotate(self.image_orig, self.rot)
            old_center = self.rect.center
            self.image = new_image
            self.rock = self.image.get_rect()
            self.rect.center = old_center

    def AI_control(self):
        # rotation
        self.rotation()
        # controls
        self.rect.x += self.speedx


class meteor_1(pygame.sprite.Sprite):
    def __init__(self, screen, y):
        super().__init__()
        self.screen = screen
        random_number = random.randint(0, 1)
        self.image_orig = rocks_large[random_number]
        self.image = rocks_large[random_number]
        # self.image_orig = pygame.transform.scale(rocks_set[random_number], (random.randrange(15, 60), random.randrange(25, 80)))
        # self.image = pygame.transform.scale(rocks_set[random_number], (random.randrange(15, 60), random.randrange(25, 80)))
        self.radius = int(self.rect.width / 3)
        # pygame.draw.circle(self.image, red, self.rect.center, self.radius)
        # self.speedx = -4
        self.speedx = random.randrange(-7, -2)
        self.hit_damage = 100
        self.rect.x = self.screen.get_width() + random.randint(0, 400)
        self.rect.y = y
        # rotation
        self.rot = 0
        self.rot_speed = 20
        self.last_update = pygame.time.get_ticks()

    def rotation(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > 50:
            self.last_update = now
            self.rot = (self.rot + self.rot_speed) % 360
            new_image = pygame.transform.rotate(self.image_orig, self.rot)
            old_center = self.rect.center
            self.image = new_image
            self.rock = self.image.get_rect()
            self.rect.center = old_center

    def AI_control(self):
        # rotation
        self.rotation()
        # controls
        self.rect.x += self.speedx
