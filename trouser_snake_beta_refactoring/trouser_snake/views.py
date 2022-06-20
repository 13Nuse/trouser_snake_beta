#! python3
import pygame

from models import Settings
from models import VideoSettings
from models import PlayerModel
from models import GameStart
from models import Colors
from models import ImageData
from models import GameOver


def background_color(self):
    VideoSettings.game_display.fill(Colors.white)
    return


def game_intro(self, game_display):
    self.game_display = game_display()
    pygame.init()

    intro = GameStart.intro
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

    def game_display(self):
        game_display = pygame.display.set_mode(VideoSettings.display_width, VideoSettings.display_height)
        return game_display


def pause():
    paused = Settings.paused()

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


def charactor_move(self, PlayerModel):
    # assigning what each key press does for player model.
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
            pause()
    print(pygame.event)  # for debugging


def charactor_sprite(self, block_size, hero_body):
    # Once key is pressed, player image will update with appropriate direction.
    if PlayerModel.direction == 'right':
        head = pygame.transform.rotate(ImageData.hero_img, PlayerModel.right)

    if PlayerModel.direction == 'left':
        head = pygame.transform.rotate(ImageData.hero_img, PlayerModel.left)

    if PlayerModel.direction == 'up':
        head = pygame.transform.rotate(ImageData.hero_img, PlayerModel.up)

    if PlayerModel.direction == 'down':
        head = pygame.transform.rotate(ImageData.hero_img, PlayerModel.down)

    VideoSettings.game_display.blit(head, (hero_body[-1][0], hero_body[-1][1]))

    for XnY_axis in hero_body[:-1]:
        # draws snake (where, color, and position[x,y,width,height])
        pygame.draw.rect(VideoSettings.game_display, Colors.brown, [XnY_axis[0], XnY_axis[1], block_size, block_size])


def Collision(PlayerModel):
    # Checks if player crashed into self.
    for each in PlayerModel.hero_body[:-1]:
        if each == PlayerModel.hero_head:
            GameOver.game_over = True

    charactor_sprite(PlayerModel.block_size, PlayerModel.hero_body)

    PlayerModel.score(PlayerModel.body_length - PlayerModel.growth)

    pygame.display.update()


def pill():
    pass


def game_over_screen(GameOver):
    # Game over screen, asking player what they want to do.
    VideoSettings.game_display.fill(Colors.black)
    VideoSettings.message_to_screen("Game Over",
                                    Colors.red,
                                    y_displace=-50,
                                    size="medium")

    VideoSettings.message_to_screen("press C to play again or Q to quit.", Colors.red)
    pygame.display.update()


def user_gameover():
    #  Checks if player crashed into outer walls.
    if PlayerModel.lead_x >= VideoSettings.display_width or PlayerModel.lead_x < 0 or PlayerModel.lead_y >= VideoSettings.display_height or PlayerModel.lead_y < 0:
        GameOver.game_over = True
        PlayerModel.direction = 'right'
        game_over_screen()

    PlayerModel.lead_x += PlayerModel.lead_x_change
    PlayerModel.lead_y += PlayerModel.lead_y_change
    pygame.display.update()


def score(self, score):
    self.score = score
    text = self.small_font.render('Score: ' + str(int(self.score) * 10), True, Colors.black)
    # displays score at top left corner
    self.game_display.blit(text, [0, 0])


def hi_score(self, score):
    pass


def game_loop():
    game_exit, game_over = (GameOver.game_exit, GameOver.game_over)
    game_intro()
    while not game_exit:
        while game_over is True:
            game_over()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_exit = True
                    game_over = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_exit = True
                        game_over = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            # game exit
            if event.type == pygame.QUIT:
                game_exit = True

        # game exit from user
        user_gameover()

        # background color(color, rect[x,y,width,height])
        background_color()

        # score for game.
        score(PlayerModel.body_length - PlayerModel.growth)

        pill_thickness = item_size

        game_display.blit(taco_img, (rand_pill_x, rand_pill_y))  # taco def goes here

        # adds length of snake after pill is eaten
        charactor_growth()

        # checks collision of snake head
        collision()

        charactor_sprite(PlayerModel.block_size, PlayerModel.hero_body)

        score(PlayerModel.body_length - PlayerModel.growth)

        pygame.display.update()

        # when you eat a pill another one shows at a random spot
        if lead_x >= rand_pill_x and lead_x <= rand_pill_x + pill_thickness:
            if lead_y >= rand_pill_y and lead_y <= rand_pill_y + pill_thickness:
                rand_pill_x, rand_pill_y = charactor_item()
                body_length += growth
            elif lead_y + block_size > rand_pill_y and lead_y + block_size < rand_pill_y:
                rand_pill_x, rand_pill_y = charactor_item()
                body_length += growth

        # uses in game time to adjust the fps
        clock.tick(FPS)

    pygame.quit()
    quit()


# pygame.display.set_icon(ImageData.favicon_img)
# pygame.display.set_caption('Trouser Snake'
