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
img_player_iconic = pygame.image.load('drone_1_blue.png')

# Font
font_name = pygame.font.match_font('arial')


class text():
    def __init__(self, screen, Text, size, x, y, color):
        font = pygame.font.Font(font_name, size)
        text_surface = font.render(Text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        screen.blit(text_surface, text_rect)


class draw_hp_bar():
    def __init__(self, screen, x, y, full_hp, current_hp):
        bar_length = 100
        bar_height = 30
        fill = current_hp / full_hp * 100
        outline_rect = pygame.Rect(x, y, bar_length, bar_height)
        fill_rect = pygame.Rect(x, y, fill, bar_height)
        pygame.draw.rect(screen, green, fill_rect)
        pygame.draw.rect(screen, white, outline_rect, 2)


class draw_icons_lives():
    def __init__(self, screen, x, lives):
        for i in range(lives):
            img = pygame.transform.scale(img_player_iconic, (30, 20))
            img_rect = img.get_rect()
            img_rect.x = x
            img_rect.y = 0
            x += 30
            screen.blit(img, img_rect)


class draw_botton():
    def __init__(self, screen, Text, x, y, width, height, color_botton, color_text, draw_condition):
        self.screen = screen
        self.width = width
        self.height = height
        self.color_botton = color_botton
        self.color_text = color_text
        self.x = x
        self.y = y
        self.speedx = 0
        self.speedy = 0
        self.Text = Text
        self.draw_condition = draw_condition
        # draw_rectangle.controls(self)
        botton_rectangle = pygame.Rect(self.x, self.y, self.width, self.height)
        if self.draw_condition:
            pygame.draw.rect(self.screen, self.color_botton, botton_rectangle)
            botton_text = text(screen, self.Text, 30, self.x + 100, self.y + 7, self.color_text)

    def controls(self):
        # initial speed set to 0
        self.speedx = 0
        self.speedy = 0
        # controls rules
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -5
            print('left')
        if keystate[pygame.K_RIGHT]:
            self.speedx = 5
            print('right')
        if keystate[pygame.K_UP]:
            self.speedy = -5
        if keystate[pygame.K_DOWN]:
            self.speedy = 5
        self.x += self.speedx
        self.y += self.speedy
        print (self.x)
