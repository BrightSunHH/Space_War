import pygame
from os import path
import SpaceRock
import Texts
import Bullets
import Explosion
import Mobship
import Player
import Planet
import random

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (200, 0, 0)
red_bright = (255, 0, 0)
green = (0, 200, 0)
green_bright = (0, 255, 0)
blue = (0, 0, 255)
blue_bright = (0, 0, 200)
yellow = (255, 255, 0)
# Colors

# Constants
FPS = 100
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Initialize pygame and create window
pygame.init()
pygame.mixer.init()
mainSurface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
pygame.display.set_caption('Space War')
clock = pygame.time.Clock()

# Load game graphics
imgs_dir = path.join(path.dirname(__file__), 'imgs')
snd_dir = path.join(path.dirname(__file__), 'sounds')
background = pygame.image.load('bk_space.png')
background_rect = background.get_rect()
menu_background = pygame.image.load('space_2.png')

# Load game sounds
explosion_sound = pygame.mixer.Sound('Explosion18.wav')
shoot_sound = pygame.mixer.Sound('Laser_Shoot25.wav')
botton_select_sound = pygame.mixer.Sound('Select.wav')
explosion_player_sound = pygame.mixer.Sound('Explosion_player.wav')
# menu_music = pygame.mixer.Sound('Sci-fi_Pulse_Loop.wav')

# Units_group initiated
units_all = pygame.sprite.Group()
units_player = pygame.sprite.Group()
units_rocks = pygame.sprite.Group()
units_bullets = pygame.sprite.Group()
units_mobships = pygame.sprite.Group()


# ------------------------------------------------

# Methods  used

# Create players


def new_player():
    x = Player.player_1(mainSurface)
    units_player.add(x)
    units_all.add(x)

# Create bullets


def shoot(self):
    bullet = Bullets.bullet_1(mainSurface, self.rect.centerx, self.rect.centery)
    units_all.add(bullet)
    units_bullets.add(bullet)

# Create rocks


def new_rock():
    choose_size = random.randint(1, 3)
    if choose_size == 1 or choose_size == 2:
        y = random.randrange(0, (SCREEN_HEIGHT - 30))
        x = SpaceRock.space_rock1(mainSurface, y)
        collision_check(x, units_rocks, False, False)
        for hit in collision_check(x, units_rocks, False, False):
            hit.rect.y += 60
            print('check1!')
        units_all.add(x)
        units_rocks.add(x)
    if choose_size == 3:
        y = random.randrange(0, (SCREEN_HEIGHT - 60))
        x = SpaceRock.space_rock2(mainSurface, y)
        collision_check(x, units_rocks, False, False)
        for hit in collision_check(x, units_rocks, False, False):
            hit.rect.y += 100
            print('check2!')
        units_all.add(x)
        units_rocks.add(x)


# Create rocks


def new_mob():
    x = Mobship.mob_ship(mainSurface)
    units_mobships.add(x)
    units_all.add(x)


# Check for collision between 2 different groups

def collision_check_groups(group1, group2, kill1, kill2):
    hits = pygame.sprite.groupcollide(group1, group2, kill1, kill2)
    return hits

# Check for collision between a unit and a group


def collision_check(unit, group, kill1, kill2):
    hits = pygame.sprite.spritecollide(unit, group, kill1, kill2)
    return hits


# ------------------------------------------------

# Start of main


clock.tick(FPS)
score = 0

# Play background music
pygame.mixer.music.load('Sci-fi_Pulse_Loop.wav')
pygame.mixer.music.set_volume(1)
pygame.mixer.music.play(-1)

# Loops
running = True


def menu():
    menu_condition = True
    start_botton_current = 1
    quit_botton_current = 1
    start_blinking = True
    quit_blinking = False
    # Create bottons

    while menu_condition:

        # Background and units on screen
        mainSurface.blit(menu_background, background_rect)
        # mainSurface.fill(black)

        # Create bottons in menu
        start_botton = Texts.draw_botton(mainSurface, 'Start Game', 300, 200, 200, 50, blue, black, True)
        quit_botton = Texts.draw_botton(mainSurface, 'Quit', 300, 300, 200, 50, blue, black, True)
        # Create a mouse location finder
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        # print (mouse)
        # print(click)

        # Conditions for mouse and bottons interaction
        mouse_start_botton_x = (300 < mouse[0] < 300 + 200)
        mouse_start_botton_y = (200 < mouse[1] < 200 + 50)
        if mouse_start_botton_x and mouse_start_botton_y:
            start_botton_shadow = Texts.draw_botton(mainSurface, 'Start Game', 300, 200, 200, 50, white, blue, True)
            # print('mouse is on start game botton')
            if click[0] == 1:
                menu_condition = False

        mouse_quit_botton_x = (300 < mouse[0] < 300 + 200)
        mouse_quit_botton_y = (300 < mouse[1] < 300 + 50)
        if mouse_quit_botton_x and mouse_quit_botton_y:
            # print('mouse is on quit game botton')
            quit_botton = Texts.draw_botton(mainSurface, 'Quit', 300, 300, 200, 50, white, blue, True)
            if click[0] == 1:
                botton_select_sound.play()
                pygame.quit()
                quit()

        # Events loop
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    start_blinking = False
                    quit_blinking = True
                    botton_select_sound.play()
                if event.key == pygame.K_UP:
                    start_blinking = True
                    quit_blinking = False
                    botton_select_sound.play()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if start_blinking:
                        menu_condition = False
                        botton_select_sound.play()
                    if quit_blinking:
                        pygame.quit()
                        quit()
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Start botton animation
        if start_blinking:
            if start_botton_current == 1:
                start_botton = Texts.draw_botton(mainSurface, 'Start Game', 300, 200, 200, 50, blue, white, True)
            if start_botton_current == 2:
                start_botton_shadow = Texts.draw_botton(mainSurface, 'Start Game', 300, 200, 200, 50, white, blue, True)
            if start_botton_current == 2:
                start_botton_current = 1
            else:
                start_botton_current += 1
        # Quit botton animation
        if quit_blinking:
            if quit_botton_current == 1:
                quit_botton = Texts.draw_botton(mainSurface, 'Quit', 300, 300, 200, 50, blue, white, True)
            if quit_botton_current == 2:
                quit_botton_shadow = Texts.draw_botton(mainSurface, 'Quit', 300, 300, 200, 50, white, blue, True)
            if quit_botton_current == 2:
                quit_botton_current = 1
            else:
                quit_botton_current += 1

        pygame.display.update()
        clock.tick(7)


menu()


def menu_resume():
    menu_resume_condition = True
    resume_botton_current = 1
    quit_botton_current = 1
    resume_blinking = True
    quit_blinking = False
    # Create bottons

    while menu_resume_condition:

        # Background and units on screen
        mainSurface.blit(menu_background, background_rect)
        # mainSurface.fill(black)

        # Create bottons in menu
        resume_botton = Texts.draw_botton(mainSurface, 'Resume', 300, 200, 200, 50, blue, black, True)
        quit_botton = Texts.draw_botton(mainSurface, 'Quit', 300, 300, 200, 50, blue, black, True)
        # Create a mouse location finder
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        # print (mouse)
        # print(click)

        # Conditions for mouse and bottons interaction
        mouse_resume_botton_x = (300 < mouse[0] < 300 + 200)
        mouse_resume_botton_y = (200 < mouse[1] < 200 + 50)
        if mouse_resume_botton_x and mouse_resume_botton_y:
            resume_botton_shadow = Texts.draw_botton(mainSurface, 'Resume', 300, 200, 200, 50, white, blue, True)
            # print('mouse is on start game botton')
            if click[0] == 1:
                menu_resume_condition = False

        mouse_quit_botton_x = (300 < mouse[0] < 300 + 200)
        mouse_quit_botton_y = (300 < mouse[1] < 300 + 50)
        if mouse_quit_botton_x and mouse_quit_botton_y:
            # print('mouse is on quit game botton')
            quit_botton = Texts.draw_botton(mainSurface, 'Quit', 300, 300, 200, 50, white, blue, True)
            if click[0] == 1:
                botton_select_sound.play()
                pygame.quit()
                quit()

        # Events loop
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    resume_blinking = False
                    quit_blinking = True
                    botton_select_sound.play()
                if event.key == pygame.K_UP:
                    resume_blinking = True
                    quit_blinking = False
                    botton_select_sound.play()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if resume_blinking:
                        menu_resume_condition = False
                        botton_select_sound.play()
                    if quit_blinking:
                        pygame.quit()
                        quit()
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Start botton animation
        if resume_blinking:
            if resume_botton_current == 1:
                resume_botton = Texts.draw_botton(mainSurface, 'Resume', 300, 200, 200, 50, blue, white, True)
            if resume_botton_current == 2:
                resume_botton_shadow = Texts.draw_botton(mainSurface, 'Resume', 300, 200, 200, 50, white, blue, True)
            if resume_botton_current == 2:
                resume_botton_current = 1
            else:
                resume_botton_current += 1
        # Quit botton animation
        if quit_blinking:
            if quit_botton_current == 1:
                quit_botton = Texts.draw_botton(mainSurface, 'Quit', 300, 300, 200, 50, blue, white, True)
            if quit_botton_current == 2:
                quit_botton_shadow = Texts.draw_botton(mainSurface, 'Quit', 300, 300, 200, 50, white, blue, True)
            if quit_botton_current == 2:
                quit_botton_current = 1
            else:
                quit_botton_current += 1

        pygame.display.update()
        clock.tick(7)


# Play background music
pygame.mixer.music.load('Vegas_Loop.wav')
pygame.mixer.music.set_volume(5)
pygame.mixer.music.play(-1)

# MyCapsule initiated and added to our all units_group
player = new_player()

# Space rock initiated and added to our all units group
for i in range(4):
    rock = new_rock()

# Background planet initiated and added to our all units group
planet = Planet.planet_1(mainSurface)
units_all.add(planet)
# Create a mob
# mob = new_mob()
count = 0
shadow_score = 0
# Game Loop
while running:

    # Events loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                # pygame.mixer.music.pause()
                menu_resume()
            if event.key == pygame.K_SPACE:
                shoot_sound.play()
                shoot(player)

    # Control rules for all units movement

    for player in units_player:
        Player.player_1.manual_control(player)
    for unit in units_rocks:
        SpaceRock.space_rock1.AI_control(unit)
    for unit in units_mobships:
        Mobship.mob_ship.AI_control_outside(unit)
    if (Planet.planet_1.AI_control(planet, shadow_score, count)):
        count = 0
        shadow_score = 0

    # Checking if mobs entered the screen and assign new controls
    for unit in units_mobships:
        if unit.rect.right <= SCREEN_WIDTH or unit.rect.top <= 0:
            Mobship.mob_ship.AI_control_inside(unit)
            if collision_check(unit, units_rocks, False, False):
                unit.speedy = 0
                unit.speedx = 0
    # Cecking collision between mobs and rocks and if so reverse direction of that mob

    # Checking if any rock passed the screen, self destructed
    for unit in units_rocks:
        if unit.rect.right <= 0:
            unit.kill()
            rock = new_rock()
            count += 1
        if unit.rect.bottom > SCREEN_HEIGHT:
            print ('check3!')
            unit.kill()
            rock = new_rock()

    # Checking collision between rocks and rocks and initiating speedy rocks
    for unit in units_rocks:
        units_rocks.remove(unit)
        if (collision_check(unit, units_rocks, False, False)):
            unit.speedx -= 5
            explosion_sound.play()
            expl_rock = Explosion.explosion(mainSurface, unit.rect.centerx, unit.rect.centery, 'rocks')
            units_all.add(expl_rock)
        units_rocks.add(unit)

    # Checking collision between rocks and bullets
    hits_2 = pygame.sprite.groupcollide(units_rocks, units_bullets, True, True, pygame.sprite.collide_circle)
    for hit in hits_2:
        new_rock()
        score += 10
        shadow_score += 10
        explosion_sound.play()
        expl_rock = Explosion.explosion(mainSurface, hit.rect.centerx, hit.rect.centery, 'rocks')
        units_all.add(expl_rock)

    # Checking collision against player
    hits_1 = pygame.sprite.groupcollide(units_player, units_rocks, False, True, pygame.sprite.collide_circle)
    for hit in hits_1:
        rock = new_rock()
        for unit in units_rocks:
            damage = unit.hit_damage
        player.hp -= damage
        explosion_player_sound.play()
        expl_player = Explosion.explosion(mainSurface, player.rect.centerx, player.rect.centery, 'rocks')
        units_all.add(expl_player)
        if player.hp <= 0:
            player.hide()
            player.lives += -1
            player.hp = player.full_hp
            if player.lives == 0:
                gameover_text = Texts.text(mainSurface, 'Game Over', 50, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, white)
                # pygame.time.wait(5000)
                running = False

    # Updating the screen
#         mainSurface.fill(black)
    # background and game units on screen
    mainSurface.blit(background, background_rect)
    units_all.update()
    units_all.draw(mainSurface)
    # Screen platform, e.g. (Score, Hp bar)
    text_1 = Texts.text(mainSurface, 'Score ' + str(score), 18, SCREEN_WIDTH / 2, 20, white)
    hp_bar = Texts.draw_hp_bar(mainSurface, 0, 20, player.full_hp, player.hp)
    lives_icons = Texts.draw_icons_lives(mainSurface, 0, player.lives)
    pygame.display.update()

# Quit when gameover is True
pygame.quit()
quit()
