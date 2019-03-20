#! python3

import pygame
import random


class Settings:
    def __init__(self, clock, FPS):
        self.clock = clock
        self.FPS = FPS

    clock = pygame.time.Clock()
    growth = 1
    FPS = 15
    # def easy_game(self):
    # self.easy = item_size * 3

    # medium = item_size * 2
    # hard = item_size
    # hi-score


class Colors:
    white = (255, 255, 255)
    black = (0, 0, 0)
    red = (255, 0, 0)
    green = (0, 155, 0)
    brown = (184, 121, 87)


class ImageData:
    favicon_img = pygame.image.load('taco.png')
    bgGame_img = pygame.image.load('bggame.jpeg')
    hero_img = pygame.image.load('snakehead.png')
    pill_img = pygame.image.load('speed.png')
    item_img = pygame.image.load('pill.png')
    taco_img = pygame.image.load('taco.png')


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

    def video_resolution(self):
        self.display_width = 800
        self.display_height = 600
        self.display_res = (self.display_width, self.display_height)
        print(self.display_res)

    def game_display(self):
        self.game_display = pygame.display.set_mode((self.display_width, self.display_height))
        pygame.display.set_icon(ImageData.favicon_img)
        pygame.display.set_caption('Trouser Snake')
        return


class InGameSettings:

    def pause(self):
        paused = True

        while paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        paused = False
                    if event.key == pygame.K_q:
                        pygame.quit()
                        quit()
            VideoSettings.game_display.fill(Colors.black)
            VideoSettings.message_to_screen("Game Paused",
                                            Colors.red,
                                            y_displace=-50,
                                            size="large")
            VideoSettings.message_to_screen("Press C to continue or Q to quit.",
                                            Colors.white,
                                            y_displace=50,
                                            size="medium")
            pygame.display.update()
            Settings.clock.tick(5)


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
        up = 0
        left = 90
        down = 180
        right = 270

    @classmethod
    def charactor_move(self):
        if pygame.event.type == pygame.KEYDOWN:
            if pygame.event.key == pygame.K_LEFT:
                PlayerModel.direction = "left"
                self.lead_x_change = -PlayerModel.block_size
                self.lead_y_change = PlayerModel.stop
            elif pygame.event.key == pygame.K_RIGHT:
                PlayerModel.direction = "right"
                self.lead_x_change = PlayerModel.block_size
                self.lead_y_change = PlayerModel.stop
            elif pygame.event.key == pygame.K_UP:
                PlayerModel.direction = "up"
                self.lead_y_change = -PlayerModel.block_size
                self.lead_x_change = PlayerModel.stop
            elif pygame.event.key == pygame.K_DOWN:
                PlayerModel.direction = "down"
                self.lead_y_change = PlayerModel.block_size
                self.lead_x_change = PlayerModel.stop
            elif pygame.event.key == pygame.K_p:
                InGameSettings.pause()
        print(pygame.event)  # for debugging

    @classmethod
    def charactor_sprite(self, block_size, hero_body):
        if PlayerModel.charactor_move.direction == 'right':
            head = pygame.transform.rotate(ImageData.hero_img, PlayerModel.right)

        if PlayerModel.charactor_move.direction == 'left':
            head = pygame.transform.rotate(ImageData.hero_img, PlayerModel.left)

        if PlayerModel.charactor_move.direction == 'up':
            head = pygame.transform.rotate(ImageData.hero_img, PlayerModel.up)

        if PlayerModel.charactor_move.direction == 'down':
            head = pygame.transform.rotate(ImageData.hero_img, PlayerModel.down)

        VideoSettings.game_display.blit(head, (hero_body[-1][0], hero_body[-1][1]))

        for XnY_axis in hero_body[:-1]:
            # draws snake (where, color, and position[x,y,width,height])
            pygame.draw.rect(VideoSettings.game_display, Colors.brown, [XnY_axis[0], XnY_axis[1], block_size, block_size])

    def charactor_growth(self):
        hero_head = []
        hero_body = []
        body_length = 1
        hero_head.append(self.lead_x)
        hero_head.append(self.lead_y)
        hero_body.append(hero_head)

        if len(hero_body) > body_length:
            del hero_body[0]

    def charactor_item(self):
        item_size = 20
        rand_pill_x = round(random.randrange(0, VideoSettings.display_width - item_size) / item_size) * item_size
        rand_pill_y = round(random.randrange(0, VideoSettings.display_height - item_size) / item_size) * item_size
        return rand_pill_x, rand_pill_y

    def score(self, score):
        self.score = score
        text = self.small_font.render('Score: ' + str(int(self.score) * 10), True, Colors.black)
        # displays score at top left corner
        self.game_display.blit(text, [0, 0])

    def model_draw():
        pass


class EnemyModel(PlayerModel):
    def __init__(self, size):
        self.size = self.item_size

    rand_pill_x, rand_pill_y = PlayerModel.charactor_item()


class GameStart:
    def game_intro():
        intro = True

        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.QUIT
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        intro = False
                    if event.key == pygame.K_q:
                        pygame.QUIT
                        quit()

            VideoSettings.game_display.fill(Colors.black)
            VideoSettings.message_to_screen('Welcome to',
                                            Colors.red,
                                            -100,
                                            size='medium'
                                            )
            VideoSettings.message_to_screen('Trouser Snake',
                                            Colors.green,
                                            size='large'
                                            )
            VideoSettings.message_to_screen('Press C to start, P to pause or Q to quit.',
                                            Colors.green,
                                            100,
                                            size='small'
                                            )

            pygame.display.update()
            Settings.clock.tick(Settings.FPS)


class GameOver:

    def user_gameover(self):
        if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
            game_over = True
            direction = 'right'

        lead_x += lead_x_change
        lead_y += lead_y_change

    def gamover(self):
        pass
