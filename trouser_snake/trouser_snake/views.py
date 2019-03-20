#! python3
import pygame

from models import Settings
from models import VideoSettings
from models import PlayerModel
from models import Colors
from models import ImageData


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


def pause():
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
            pause()
    print(pygame.event)  # for debugging


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
