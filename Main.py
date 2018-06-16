import pygame
import os
import random
import SpaceRock
import draw
import Bullets
import Explosion
import Player
import Planet
import Mobship

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
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'imgs')
sound_folder = os.path.join(game_folder, 'sounds')
background = pygame.image.load(os.path.join(img_folder, 'bk_space.png'))
background_rect = background.get_rect()
menu_background = pygame.image.load(os.path.join(img_folder, ('space_2.png')))

# Load game sounds
explosion_sound = pygame.mixer.Sound(os.path.join(sound_folder, 'Explosion18.wav'))
shoot_sound = pygame.mixer.Sound(os.path.join(sound_folder, 'Laser_Shoot25.wav'))
botton_select_sound = pygame.mixer.Sound(os.path.join(sound_folder, 'Select.wav'))
explosion_player_sound = pygame.mixer.Sound(os.path.join(sound_folder, 'Explosion_player.wav'))
shoot_sound_2 = pygame.mixer.Sound(os.path.join(sound_folder, 'mob_Laser.wav'))
explosion_sound_2 = pygame.mixer.Sound(os.path.join(sound_folder, 'mob_Laser.wav'))
explosion_sound_3 = pygame.mixer.Sound(os.path.join(sound_folder, 'Explosion13.wav'))

# menu_music = pygame.mixer.Sound('Sci-fi_Pulse_Loop.wav')

# Units_group initiated
units_all = pygame.sprite.Group()
units_player = pygame.sprite.Group()
units_rocks = pygame.sprite.Group()
units_bullets = pygame.sprite.Group()
units_bullets_mob = pygame.sprite.Group()
units_planets = pygame.sprite.Group()
units_mobships = pygame.sprite.Group()


# ------------------------------------------------

# Methods used

# Create players


def new_player():
    x = Player.player_1(mainSurface)
    units_player.add(x)
    units_all.add(x)

# Create planet


def new_planet():
    x = Planet.planet_1(mainSurface)
    units_planets.add(x)
    units_all.add(x)

# Create player bullets


def shoot_player(self):
    bullet = Bullets.bullet_1(mainSurface, self.rect.centerx, self.rect.centery)
    units_bullets.add(bullet)
    units_all.add(bullet)


# Create enemy bullets


# def shoot_enemy(self):
#     bullet = Bullets.bullet_2(mainSurface, self.rect.x, self.rect.y)
#     units_bullets_mob.add(bullet)
#     units_all.add(bullet)

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


# Create a mob


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


def new():
    # Player initiated and added to our all units_group
    player = new_player()
    # Spacerocks initiated and added to our all units group
    for i in range(7):
        rock = new_rock()

    # Planet initiated and added to our all units group
    planet = new_planet()

    # Create a mob
    mob = new_mob()


def menu():

    # Play background music
    pygame.mixer.music.load(os.path.join(sound_folder, 'Sci-fi_Pulse_Loop.wav'))
    pygame.mixer.music.set_volume(1)
    pygame.mixer.music.play(-1)

    # Create conditions
    menu_condition = True
    start_botton_current = 1
    quit_botton_current = 1
    start_blinking = True
    quit_blinking = False

    # Menu loop
    while menu_condition:

        # Background and units on screen
        mainSurface.blit(menu_background, background_rect)
        # mainSurface.fill(black)

        # Create bottons in menu
        start_botton = draw.draw_botton(mainSurface, 'Start Game', 300, 200, 200, 50, blue, black, True)
        quit_botton = draw.draw_botton(mainSurface, 'Quit', 300, 300, 200, 50, blue, black, True)
        # Create a mouse location finder
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        # print (mouse)
        # print(click)

        # Conditions for mouse and bottons interaction
        mouse_start_botton_x = (300 < mouse[0] < 300 + 200)
        mouse_start_botton_y = (200 < mouse[1] < 200 + 50)
        if mouse_start_botton_x and mouse_start_botton_y:
            start_botton_shadow = draw.draw_botton(mainSurface, 'Start Game', 300, 200, 200, 50, white, blue, True)
            # print('mouse is on start game botton')
            if click[0] == 1:
                menu_condition = False

        mouse_quit_botton_x = (300 < mouse[0] < 300 + 200)
        mouse_quit_botton_y = (300 < mouse[1] < 300 + 50)
        if mouse_quit_botton_x and mouse_quit_botton_y:
            # print('mouse is on quit game botton')
            quit_botton = draw.draw_botton(mainSurface, 'Quit', 300, 300, 200, 50, white, blue, True)
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
                start_botton = draw.draw_botton(mainSurface, 'Start Game', 300, 200, 200, 50, blue, white, True)
            if start_botton_current == 2:
                start_botton_shadow = draw.draw_botton(mainSurface, 'Start Game', 300, 200, 200, 50, white, blue, True)
            if start_botton_current == 2:
                start_botton_current = 1
            else:
                start_botton_current += 1
        # Quit botton animation
        if quit_blinking:
            if quit_botton_current == 1:
                quit_botton = draw.draw_botton(mainSurface, 'Quit', 300, 300, 200, 50, blue, white, True)
            if quit_botton_current == 2:
                quit_botton_shadow = draw.draw_botton(mainSurface, 'Quit', 300, 300, 200, 50, white, blue, True)
            if quit_botton_current == 2:
                quit_botton_current = 1
            else:
                quit_botton_current += 1

        pygame.display.update()
        clock.tick(7)


def menu_resume():

    # Play background music
    pygame.mixer.music.load(os.path.join(sound_folder, 'Sci-fi_Pulse_Loop.wav'))
    pygame.mixer.music.set_volume(1)
    pygame.mixer.music.play(-1)

    # Create conditions
    menu_resume_condition = True
    resume_botton_current = 1
    quit_botton_current = 1
    resume_blinking = True
    quit_blinking = False

    # Menu loop
    while menu_resume_condition:

        # Background and units on screen
        mainSurface.blit(menu_background, background_rect)

        # Create bottons in menu
        resume_botton = draw.draw_botton(mainSurface, 'Resume', 300, 200, 200, 50, blue, black, True)
        quit_botton = draw.draw_botton(mainSurface, 'Quit', 300, 300, 200, 50, blue, black, True)
        # Create a mouse location finder
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        # print (mouse)
        # print(click)

        # Conditions for mouse and bottons interaction
        mouse_resume_botton_x = (300 < mouse[0] < 300 + 200)
        mouse_resume_botton_y = (200 < mouse[1] < 200 + 50)
        if mouse_resume_botton_x and mouse_resume_botton_y:
            resume_botton_shadow = draw.draw_botton(mainSurface, 'Resume', 300, 200, 200, 50, white, blue, True)
            # print('mouse is on start game botton')
            if click[0] == 1:
                menu_resume_condition = False

        mouse_quit_botton_x = (300 < mouse[0] < 300 + 200)
        mouse_quit_botton_y = (300 < mouse[1] < 300 + 50)
        if mouse_quit_botton_x and mouse_quit_botton_y:
            # print('mouse is on quit game botton')
            quit_botton = draw.draw_botton(mainSurface, 'Quit', 300, 300, 200, 50, white, blue, True)
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
                resume_botton = draw.draw_botton(mainSurface, 'Resume', 300, 200, 200, 50, blue, white, True)
            if resume_botton_current == 2:
                resume_botton_shadow = draw.draw_botton(mainSurface, 'Resume', 300, 200, 200, 50, white, blue, True)
            if resume_botton_current == 2:
                resume_botton_current = 1
            else:
                resume_botton_current += 1
        # Quit botton animation
        if quit_blinking:
            if quit_botton_current == 1:
                quit_botton = draw.draw_botton(mainSurface, 'Quit', 300, 300, 200, 50, blue, white, True)
            if quit_botton_current == 2:
                quit_botton_shadow = draw.draw_botton(mainSurface, 'Quit', 300, 300, 200, 50, white, blue, True)
            if quit_botton_current == 2:
                quit_botton_current = 1
            else:
                quit_botton_current += 1

        pygame.display.update()
        clock.tick(7)

# ---------------------------------
# Game loop
# ---------------------------------


def game_loop():

    new()

    # Create game loop conditions and score
    running = True
    score = 0
    count = 0
    shadow_score = 0
    rocks_condition = True
    bullets_exist = False
    dialogue = True
    music_play = True
    stage_1_end = False
    explosion_counter = 0

    # Play background music
    def music_1(condition):
        if condition:
            pygame.mixer.music.load(os.path.join(sound_folder, 'Vegas_Loop.wav'))
            pygame.mixer.music.set_volume(.5)
            pygame.mixer.music.play(-1)
        else:
            pygame.mixer.music.load(os.path.join(sound_folder, 'Serotonin.wav'))
            pygame.mixer.music.set_volume(1)
            pygame.mixer.music.play(-1)

    # Game Loop
    while running:
        # Set FPS
        dt = clock.tick(FPS) / 1000
        mainSurface.blit(background, background_rect)
        if music_play and rocks_condition:
            music_1(True)
            music_play = False

        if not music_play and not rocks_condition:
            music_1(False)
            music_play = True
        if score > 1500:
            rocks_condition = False

        # Events loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if dialogue:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        dialogue = False
            elif event.type == pygame.KEYDOWN and not dialogue:
                if event.key == pygame.K_ESCAPE:
                    # pygame.mixer.music.pause()
                    menu_resume()
                if event.key == pygame.K_SPACE:
                    shoot_sound.play()
                    shoot_sound.set_volume(.3)
                    shoot_player(player)
                if event.key == pygame.K_RETURN and dialogue:
                    dialogue = False

        # Control rules for all units movement
        for player in units_player:
            if not dialogue and not stage_1_end:
                Player.player_1.manual_control(player)
        for unit in units_rocks:
            if not dialogue:
                SpaceRock.space_rock1.AI_control(unit)
        if not rocks_condition:
            for unit in units_mobships:
                if not dialogue:
                    Mobship.mob_ship.AI_control_outside(unit)
        for planet in units_planets:
            Planet.planet_1.AI_control(planet, shadow_score, count)
            count = 0
            shadow_score = 0

        # Checking if mobs entered the screen and assign new controls and assign bullet
        for unit in units_mobships:
            if unit.rect.right <= SCREEN_WIDTH or unit.rect.top <= 0:
                Mobship.mob_ship.AI_control_inside(unit)
                if (unit.rect.left < SCREEN_WIDTH / 2 + 200) and not bullets_exist:
                    super_bullet = Bullets.bullet_2(mainSurface, unit.rect.left, unit.rect.centery)
                    shoot_sound_2.play()
                    shoot_sound_2.set_volume(.2)
                    units_bullets_mob.add(super_bullet)
                    units_all.add(super_bullet)
                    bullets_exist = True
                if bullets_exist:
                    expl_bullet = Explosion.explosion(mainSurface, super_bullet.rect.left, super_bullet.rect.centery, 'small')
                    units_all.add(expl_bullet)
                if len(units_bullets_mob) == 0:
                    bullets_exist = False

        # Checking if any rock passed the screen to apply self destruct
        for unit in units_rocks:
            if unit.rect.right <= 0:
                unit.kill()
                score += 10
                if rocks_condition:
                    rock = new_rock()
                count += 1
            if unit.rect.bottom > SCREEN_HEIGHT:
                print ('check3!')
                unit.kill()
                if rocks_condition:
                    rock = new_rock()

        # Checking collision between rocks and rocks and initiating speedy rocks
        for unit in units_rocks:
            units_rocks.remove(unit)
            if (collision_check(unit, units_rocks, False, False)) and unit.rect.x <= SCREEN_WIDTH:
                unit.speedx -= 5
                explosion_sound.set_volume(.2)
                explosion_sound.play()
                expl_rock = Explosion.explosion(mainSurface, unit.rect.centerx, unit.rect.centery, 'large')
                units_all.add(expl_rock)
            units_rocks.add(unit)

        # Checking collision between rocks and bullets
        hits_2 = pygame.sprite.groupcollide(units_rocks, units_bullets, True, True, pygame.sprite.collide_circle)
        for hit in hits_2:
            if rocks_condition:
                new_rock()
            score += 10
            shadow_score += 10
            explosion_sound.set_volume(.2)
            explosion_sound.play()
            expl_rock = Explosion.explosion(mainSurface, hit.rect.centerx, hit.rect.centery, 'large')
            units_all.add(expl_rock)

        # Checking collision between player and rocks
        hits_1 = pygame.sprite.groupcollide(units_player, units_rocks, False, True, pygame.sprite.collide_circle)
        for hit in hits_1:
            rock = new_rock()
            for unit in units_rocks:
                damage = unit.hit_damage
            player.hp -= damage
            explosion_player_sound.play()
            expl_player = Explosion.explosion(mainSurface, player.rect.centerx, player.rect.centery, 'large')
            units_all.add(expl_player)
            if player.hp <= 0:
                player.hide()
                player.lives += -1
                player.hp = player.full_hp
                if player.lives == 0:
                    running = False

        # Check collision between player ship and enemy bullets
        if collision_check_groups(units_player, units_bullets_mob, False, True):
            player.hp -= 100
            explosion_player_sound.play()
            expl_player = Explosion.explosion(mainSurface, player.rect.centerx, player.rect.centery, 'large')
            units_all.add(expl_player)
            if player.hp <= 0:
                player.hide()
                player.lives += -1
                player.hp = player.full_hp
                if player.lives == 0:
                    running = False

        # Check collision between player bullets and enemy bullets
        if collision_check_groups(units_bullets, units_bullets_mob, True, False):
            pass

        # Check collision between player bullets and enemy ship
        if collision_check_groups(units_mobships, units_bullets, False, True):
            for unit in units_mobships:
                unit.hp -= 100
                expl_mob_ship = Explosion.explosion(mainSurface, unit.rect.centerx, unit.rect.centery, 'large')
                explosion_sound_2.play()
                units_all.add(expl_mob_ship)
                print (unit.hp)
                if unit.hp <= 0:
                    stage_1_end = True

        # Explosion of boss when dead
        if stage_1_end:
            for unit in units_bullets_mob:
                unit.kill()
            for unit in units_bullets:
                unit.kill()
        if explosion_counter < 5 and stage_1_end:
            clock.tick(3)
            for unit in units_mobships:
                if explosion_counter == 0:
                    expl_mob_ship = Explosion.explosion(mainSurface, unit.rect.right, unit.rect.centery, 'small')
                    units_all.add(expl_mob_ship)
                    explosion_sound_3.play()
                    explosion_counter += 1
                    print('explosion of boss 0')
                elif explosion_counter == 1:
                    expl_mob_ship = Explosion.explosion(mainSurface, unit.rect.left, unit.rect.centery, 'large')
                    units_all.add(expl_mob_ship)
                    explosion_sound_3.play()
                    explosion_counter += 1
                    print('explosion of boss 1')
                elif explosion_counter == 2:
                    expl_mob_ship = Explosion.explosion(mainSurface, unit.rect.right, unit.rect.centery, 'small')
                    units_all.add(expl_mob_ship)
                    explosion_sound_3.play()
                    explosion_counter += 1
                elif explosion_counter == 3:
                    expl_mob_ship = Explosion.explosion(mainSurface, unit.rect.left, unit.rect.centery, 'large')
                    units_all.add(expl_mob_ship)
                    explosion_sound_3.play()
                    explosion_counter += 1
                elif explosion_counter == 4:
                    expl_mob_ship = Explosion.explosion(mainSurface, unit.rect.right, unit.rect.centery, 'small')
                    explosion_sound_3.play()
                    units_all.add(expl_mob_ship)
                    explosion_counter += 1
                    unit.kill()

        # Background and game units on screen
        units_all.update()
        units_all.draw(mainSurface)
        if dialogue:
            dialogue_1 = draw.dialogue(mainSurface, "Welcome this is my first game. Press Enter to continue! ", 0, 400, SCREEN_WIDTH, 300, blue, white, True)
        # Screen platform, e.g. (Score, Hp bar)
        text_1 = draw.text(mainSurface, 'Score ' + str(score), 18, SCREEN_WIDTH / 2, 20, white)
        hp_bar = draw.draw_hp_bar(mainSurface, 0, 20, player.full_hp, player.hp)
        lives_icons = draw.draw_icons_lives(mainSurface, 0, player.lives)
        if explosion_counter == 5:
            text_2 = draw.text(mainSurface, 'You Win', 40, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, blue_bright)
        pygame.display.update()


def game_over():
    # Play background music
    pygame.mixer.music.load(os.path.join(sound_folder, 'Sci-fi_Pulse_Loop.wav'))
    pygame.mixer.music.set_volume(1)
    pygame.mixer.music.play(-1)
    # Gameover condition
    gameover = True
    # Create conditions
    continue_botton_current = 1
    quit_botton_current = 1
    continue_blinking = True
    quit_blinking = False

    # Gameover loop
    while gameover:

        # Background
        mainSurface.blit(menu_background, background_rect)

        # Initiate text and buttons
        continue_botton = draw.draw_botton(mainSurface, 'Continue', 300, 200, 200, 50, blue, black, True)
        quit_botton = draw.draw_botton(mainSurface, 'Quit', 300, 300, 200, 50, blue, black, True)
        gameover_text = draw.text(mainSurface, 'Game Over', 90, SCREEN_WIDTH / 2, 40, white)

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        # print (mouse)
        # print(click)

        # Conditions for mouse and bottons interaction
        mouse_resume_botton_x = (300 < mouse[0] < 300 + 200)
        mouse_resume_botton_y = (200 < mouse[1] < 200 + 50)
        if mouse_resume_botton_x and mouse_resume_botton_y:
            continue_botton_shadow = draw.draw_botton(mainSurface, 'Continue', 300, 200, 200, 50, white, blue, True)
            # print('mouse is on start game botton')
            if click[0] == 1:
                gameover = False

        mouse_quit_botton_x = (300 < mouse[0] < 300 + 200)
        mouse_quit_botton_y = (300 < mouse[1] < 300 + 50)
        if mouse_quit_botton_x and mouse_quit_botton_y:
            # print('mouse is on quit game botton')
            quit_botton = draw.draw_botton(mainSurface, 'Quit', 300, 300, 200, 50, white, blue, True)
            if click[0] == 1:
                botton_select_sound.play()
                pygame.quit()
                quit()

        # Events loop
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    continue_blinking = False
                    quit_blinking = True
                    botton_select_sound.play()
                if event.key == pygame.K_UP:
                    continue_blinking = True
                    quit_blinking = False
                    botton_select_sound.play()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if continue_blinking:
                        gameover = False
                        botton_select_sound.play()
                    if quit_blinking:
                        pygame.quit()
                        quit()
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Continue botton animation
        if continue_blinking:
            if continue_botton_current == 1:
                continue_botton = draw.draw_botton(mainSurface, 'Continue', 300, 200, 200, 50, blue, white, True)
            if continue_botton_current == 2:
                continue_botton_shadow = draw.draw_botton(mainSurface, 'Continue', 300, 200, 200, 50, white, blue, True)
            if continue_botton_current == 2:
                continue_botton_current = 1
            else:
                continue_botton_current += 1
        # Quit botton animation
        if quit_blinking:
            if quit_botton_current == 1:
                quit_botton = draw.draw_botton(mainSurface, 'Quit', 300, 300, 200, 50, blue, white, True)
            if quit_botton_current == 2:
                quit_botton_shadow = draw.draw_botton(mainSurface, 'Quit', 300, 300, 200, 50, white, blue, True)
            if quit_botton_current == 2:
                quit_botton_current = 1
            else:
                quit_botton_current += 1

        # Update screen
        pygame.display.update()
        clock.tick(7)


# Execution
menu()
game_loop()
game_over()


# Quit when game is not running
pygame.quit()
quit()
