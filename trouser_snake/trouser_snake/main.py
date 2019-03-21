#! python3
import pygame
from models import GameOver
import views

# Start screen
p = views


p.score()
p.paused()

# game loop


def game_loop():
    p.game_intro()
    game_exit, game_over = GameOver()

    while not game_exit:
        while game_over is True:
            p.game_over()
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
        if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
            game_over = True
            direction = 'right'

        lead_x += lead_x_change
        lead_y += lead_y_change

        # background color(color, rect[x,y,width,height])
        p.background_color()

        pill_thickness = item_size

        game_display.blit(taco_img, (rand_pill_x, rand_pill_y))  # taco def goes here

        # adds length of snake after pill is eaten
        p.charactor_growth()

        # checks collision of snake head
        for each in hero_body[:-1]:
            if each == hero_head:
                game_over = True

        charactor_sprite(block_size, hero_body)

        score(body_length - growth)

        pygame.display.update()

        # when you eat a pill another on shows at a random spot
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


if __name__ == '__main__':
    pass
