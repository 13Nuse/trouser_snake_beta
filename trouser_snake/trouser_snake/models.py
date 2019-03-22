#! python3

import pygame
import random
import os


class Settings:
    def __init__(self, clock, FPS, paused):
        self.clock = clock
        self.FPS = FPS
        self.paused = paused

    def clock(self):
        self.clock = pygame.time.Clock()

    def FPS(self):
        self.FPS = 15

    def paused(self):
        return True

    # def easy_game(self):
    # self.easy = item_size * 3
    # medium = item_size * 2
    # hard = item_size


class Colors:
    white = (255, 255, 255)
    black = (0, 0, 0)
    red = (255, 0, 0)
    green = (0, 155, 0)
    brown = (184, 121, 87)


class ImageData:
    def __init__(self, images):
        self.images = images

    favicon_img = pygame.image.load(os.path.join('data', 'taco.png'))
    bgGame_img = pygame.image.load(os.path.join('data', 'bggame.jpeg'))
    hero_img = pygame.image.load(os.path.join('data', 'snakehead.png'))
    pill_img = pygame.image.load(os.path.join('data', 'speed.png'))
    item_img = pygame.image.load(os.path.join('data', 'pill.png'))
    taco_img = pygame.image.load(os.path.join('data', 'taco.png'))


class VideoSettings:
    def __init__(self, small, medium, large):
        self.small_font = small
        self.medium_font = medium
        self.large_font = large

    def small_font(self):
        self.small_font = pygame.font.SysFont('georgia', 25)
        return self.small_font

    def medium_font(self):
        self.medium_font = pygame.font.SysFont('georgia', 35)
        return self.medium_font

    def large_font(self):
        self.large_font = pygame.font.SysFont('georgia', 45)
        return self.large_font

    def text_objects(self, text, color, size):
        if size == 'small':
            text_surface = self.small_font.render(text, True, color)
        elif size == 'medium':
            text_surface = self.medium_font.render(text, True, color)
        elif size == 'large':
            text_surface = self.large_font.render(text, True, color)
        return text_surface, text_surface.get_rect()

    def message_to_screen(self, msg, color, y_displace=0, size='small'):
        text_surf, text_rect = self.text_objects(msg, color, size)
        text_rect.center = (self.display_width / 2), (self.display_height / 2) + y_displace  # centers msg then moves it to y pos.
        self.game_display.blit(text_surf, text_rect)

    def game_display(self, game_display):
        self.game_display = pygame.display()

    def video_resolution(self):
        self.display_width = 800
        self.display_height = 600
        self.display_res = self.game_display.set_mode(self.display_width, self.display_height)
        print(self.display_res)


class PlayerModel:
    def __init__(self, up, left, down, right):
        self.up = up
        self.left = left
        self.down = down
        self.right = right
        self.block_size = 20
        self.lead_x = VideoSettings.video_resolution.display_width / 2
        self.lead_y = VideoSettings.video_resolution.display_height / 2
        self.lead_x_change = self.block_size
        self.lead_y_change = 0
        self.direction = 'right'
        self.stop = 0
        self.growth = 1
        up = 0
        left = 90
        down = 180
        right = 270

    def charactor_growth(self):
        self.hero_head = []
        self.hero_body = []
        self.body_length = 1
        self.hero_head.append(self.lead_x)
        self.hero_head.append(self.lead_y)
        self.hero_body.append(self.hero_head)

        if len(self.hero_body) > self.body_length:
            del self.hero_body[0]

    def charactor_item(self):
        item_size = 20
        rand_pill_x = round(random.randrange(0, VideoSettings.display_width - item_size) / item_size) * item_size
        rand_pill_y = round(random.randrange(0, VideoSettings.display_height - item_size) / item_size) * item_size
        return rand_pill_x, rand_pill_y

    def power_item():
        pass

    def model_draw():
        pass


class EnemyModel(PlayerModel):
    def __init__(self, size):
        self.size = size
        PlayerModel.charactor_item(self.size)


class GameStart:
    def __init__(self, intro):
        self.intro = intro

    def intro(self):
        return True


class GameOver:
    def __init__(self, game_exit, game_over):
        self.game_exit = game_exit
        self.game_over = game_over

    def game_exit(self):
        return False

    def game_over(self):
        return False
