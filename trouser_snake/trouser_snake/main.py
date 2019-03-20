#! python3
import pygame

import views

# Start screen


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

        game_display.fill(black)
        message_to_screen('Welcome to',
                          red,
                          -100,
                          'medium'
                          )
        message_to_screen('Trouser Snake',
                          green,
                          size='large'
                          )
        message_to_screen('Press C to start, P to pause or Q to quit.',
                          green,
                          100,
                          'small'
                          )

        pygame.display.update()
        clock.tick(FPS)


# snake charactor
def charactor_sprite(block_size, hero_body):
    if direction == 'right':
        head = pygame.transform.rotate(hero_img, 270)

    if direction == 'left':
        head = pygame.transform.rotate(hero_img, 90)

    if direction == 'up':
        head = pygame.transform.rotate(hero_img, 0)

    if direction == 'down':
        head = pygame.transform.rotate(hero_img, 180)

    game_display.blit(head, (hero_body[-1][0], hero_body[-1][1]))

    for XnY_axis in hero_body[:-1]:
        # draws snake (where, color, and position[x,y,width,height])
        pygame.draw.rect(game_display, brown, [XnY_axis[0], XnY_axis[1], block_size, block_size])


def charactor_item():
    rand_pill_x = round(random.randrange(0, display_width - item_size) / item_size) * item_size
    rand_pill_y = round(random.randrange(0, display_height - item_size) / item_size) * item_size
    return rand_pill_x, rand_pill_y


# I'll do this one day
def power_item():
    pass


def score(score):
    text = small_font.render('Score: ' + str(int(score) * 10), True, black)
    # displays score at top left corner
    game_display.blit(text, [0, 0])


# renders text sizes and style
def text_objects(text, color, size):
    if size == 'small':
        text_surface = small_font.render(text, True, color)
    elif size == 'medium':
        text_surface = medium_font.render(text, True, color)
    elif size == 'large':
        text_surface = large_font.render(text, True, color)
    return text_surface, text_surface.get_rect()


# sends game messages to screen
def message_to_screen(msg, color, y_displace=0, size='small'):
    text_surf, text_rect = text_objects(msg, color, size)
    text_rect.center = (display_width / 2), (display_height / 2) + y_displace
    game_display.blit(text_surf, text_rect)


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
        game_display.fill(black)
        message_to_screen("Game Paused",
                          red,
                          y_displace=-50,
                          size="large")
        message_to_screen("Press C to continue or Q to quit.",
                          white,
                          y_displace=50,
                          size="medium")
        pygame.display.update()
        clock.tick(5)


# game loop
def game_loop():
    global direction
    game_exit = False
    game_over = False

    lead_x = display_width / 2
    lead_y = display_height / 2
    lead_x_change = block_size
    lead_y_change = 0

    hero_body = []
    body_length = 1

    rand_pill_x, rand_pill_y = charactor_item()

    while not game_exit:

        while game_over is True:
            game_display.fill(black)
            message_to_screen("Game Over",
                              red,
                              y_displace=-50,
                              size="medium")

            message_to_screen("press C to play again or Q to quit.", red)
            pygame.display.update()

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

            # user input
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    direction = "left"
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    direction = "right"
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    direction = "up"
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    direction = "down"
                    lead_y_change = block_size
                    lead_x_change = 0
                elif event.key == pygame.K_p:
                    pause()
            print(event)  # for debugging

        # game exit from user
        if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
            game_over = True
            direction = 'right'

        lead_x += lead_x_change
        lead_y += lead_y_change

        # background color(color, rect[x,y,width,height])
        game_display.fill(white)

        pill_thickness = item_size

        game_display.blit(taco_img, (rand_pill_x, rand_pill_y))

        # adds length of snake after pill is eaten
        hero_head = []
        hero_head.append(lead_x)
        hero_head.append(lead_y)
        hero_body.append(hero_head)

        if len(hero_body) > body_length:
            del hero_body[0]

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
    game_intro()
    game_loop()
