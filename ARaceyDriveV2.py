import pygame
import time
import random
import ClassObjects as CO


# Pygame data
pygame.init()
game_display = pygame.display.set_mode((CO.display_width, CO.display_height))
pygame.display.set_caption("A Racey Drive")
pygame.mixer.music.load("Energy.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play()
clock = pygame.time.Clock()


def display_score():
    font = pygame.font.SysFont("georgia", 25)
    text1 = font.render("High Score: " + str(CO.high_score), True, CO.white)
    text2 = font.render("Dodged:     " + str(CO.score), True, CO.white)
    text3 = font.render("Lives:      " + str(CO.lives), True, CO.white)
    game_display.blit(text1, (0, 0))
    game_display.blit(text2, (0, 20))
    game_display.blit(text3, (0, 40))


def message_display(text, size=85):
    """Used in the crashed screen"""
    large_text = pygame.font.SysFont("georgia", size)
    text_surface = large_text.render(text, True, CO.black)
    text_rect = text_surface.get_rect()
    text_rect.center = ((CO.display_width/2), (CO.display_height/2))
    game_display.blit(text_surface, text_rect)

    pygame.display.update()


def crash(thing_list):
    # Base messages
    base1 = "You Can Do It"
    base2 = "Keep Trying"
    base = [base1, base2]

    # If almost high
    almost1 = "Almost There"
    almost2 = "You Can Do It"
    almost3 = "So Close"
    almost = [almost1, almost2, almost3]

    # If current high score
    hs1 = "Check You Out"
    hs2 = "Keep Going!"
    hs = [hs1, hs2]

    messages = []
    if CO.score == CO.high_score:
        messages = hs
    elif CO.score > CO.high_score - 10:
        messages = almost
    else:
        messages = base

    message_display(random.choice(messages))
    for thing in thing_list:
        thing.reset_pos()
        thing.reduce_numbers()
    if CO.Divider.speed > 20:
        CO.Divider.speed = CO.Divider.speed / 2
    else:
        CO.Divider.speed = 10
    CO.score = int(CO.score / 2)
    CO.lives -= 1
    time.sleep(.5)


def continue_screen():
    to_continue = True
    keep_playing = True

    # Display Encouragement
    game_display.fill(CO.lt_gray)
    if CO.score == CO.high_score:
        message_display("Great Run")
    elif CO.score > CO.high_score - 10:
        message_display("So Close")
    elif CO.score > CO.high_score - 25:
        message_display("Keep Pushing")
    else:
        message_display("Don't Give Up")
    pygame.display.update()
    time.sleep(.75)

    # display score
    game_display.fill(CO.lt_gray)
    message_display("Score: " + str(CO.score))
    pygame.display.update()
    time.sleep(.75)

    # display high score
    game_display.fill(CO.lt_gray)
    message_display("High Score: " + str(CO.high_score), 80)
    time.sleep(.75)

    while to_continue:
        # prompt for continue
        game_display.fill(CO.lt_gray)
        message_display("Continue? (y/n)", 75)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y or event.key == pygame.K_RETURN:
                    keep_playing = True
                    to_continue = False
                if event.key == pygame.K_n or event.key == pygame.K_ESCAPE:
                    keep_playing = False
                    to_continue = False

    return keep_playing


def game_loop():
    # sets base RUN variables
    keep_playing = True
    CO.update_local_high_score_from_file()

    while keep_playing:  # Outer loop for continue screen
        # sets base GAME variables
        CO.score = 0
        CO.lives = 3
        keep_playing = True
        improvable = False

        # starter pieces
        player = CO.Car()
        thing_list = [CO.Thing(CO.greens, 1)]

        # Lane dividers
        line_list = []
        for i in range(11):
            line_list.append(CO.Divider(CO.display_width*0.2, i*97))
            line_list.append(CO.Divider(CO.display_width*0.4, i*97))
            line_list.append(CO.Divider(CO.display_width*0.6, i*97))
            line_list.append(CO.Divider(CO.display_width*0.8, i*97))

        while CO.lives > 0:  # Inner loop for game
            # game logic
            stage = int(CO.score / 50)

            # display background
            if stage == 0:
                game_display.fill(CO.dk_green)
            elif stage == 1:
                game_display.fill(CO.green)
            elif stage == 2:
                game_display.fill(CO.dk_blue)
            if stage == 3:
                game_display.fill(CO.blue)
            elif stage == 4:
                game_display.fill(CO.dk_red)
            elif stage > 4:
                game_display.fill(CO.red)

            # Need to look into adding green to edges and white dividers here
            pygame.draw.rect(game_display, CO.dk_gray, [10, 0, CO.display_width - 20, CO.display_height])
            for line in line_list:
                line.update()
                pygame.draw.rect(game_display, line.color, [int(line.x), int(line.y), line.width, line.height])

            # Thing logic
            # move things
            for thing in thing_list:
                crashed = thing.update(player)
                pygame.draw.rect(game_display, thing.color, [int(thing.x), int(thing.y), thing.width, thing.height])
                if crashed:
                    crash(thing_list)

            # adds new things at certain points
            if CO.score >= CO.start2 and len(thing_list) == 1:
                thing_list.append(CO.Thing(CO.blues, 2))
            if CO.score >= CO.start3 and len(thing_list) == 2:
                thing_list.append(CO.Thing(CO.reds, 3))

            # display score
            display_score()

            # player logic
            # check for speed increase
            if improvable and CO.score % 10 == 0:
                player.upgrade()
                improvable = False
            if CO.score % 10 == 1:
                improvable = True
            # update player pos
            player.update()
            game_display.blit(player.image, (player.x, player.y))

            # update screen
            pygame.display.update()
            clock.tick(CO.FPS)

        """Continue screen"""
        keep_playing = continue_screen()


if __name__ == "__main__":
    game_loop()

pygame.quit()
quit()
