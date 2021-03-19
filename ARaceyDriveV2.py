import pygame
import time
import ClassObjects as CO


# Pygame data
pygame.init()
game_display = pygame.display.set_mode((CO.display_width, CO.display_height))
pygame.display.set_caption("A Racey Drive")
pygame.mixer.music.load("Energy.mp3")
pygame.mixer.music.play()
clock = pygame.time.Clock()


def display_score():
    font = pygame.font.SysFont("georgia", 25)
    text1 = font.render("Dodged:     " + str(CO.score), True, CO.white)
    text2 = font.render("High Score: " + str(CO.high_score), True, CO.white)
    game_display.blit(text1, (0, 0))
    game_display.blit(text2, (0, 20))


def message_display(text):
    """Used in the crashed screen"""
    large_text = pygame.font.SysFont("georgia", 115)
    text_surface = large_text.render(text, True, CO.black)
    text_rect = text_surface.get_rect()
    text_rect.center = ((CO.display_width/2), (CO.display_height/2))
    game_display.blit(text_surface, text_rect)

    pygame.display.update()


def crash(thing_list):
    message_display("You Can Do It")
    for thing in thing_list:
        thing.reset_pos()
        thing.speed = thing.speed / 2
    CO.Divider.speed = 10
    CO.score = int(CO.score / 2)
    CO.lives -= 1
    time.sleep(.5)
    # game_loop()


def game_loop():
    CO.score = 0
    thing_list = [CO.Thing(CO.greens, 1)]
    line_list = []
    for i in range(11):
        line_list.append(CO.Divider(CO.display_width*0.2, i*97))
        line_list.append(CO.Divider(CO.display_width*0.4, i*97))
        line_list.append(CO.Divider(CO.display_width*0.6, i*97))
        line_list.append(CO.Divider(CO.display_width*0.8, i*97))
    crashed = False
    improvable = False
    player = CO.Car()

    # Thinking of adding an outer loop here that will deal with the reset screen
    while CO.lives > 0:
        # game logic

        # background
        game_display.fill(CO.dk_green)

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
        if CO.score == CO.start2 and len(thing_list) == 1:
            thing_list.append(CO.Thing(CO.blues, 2))
        if CO.score == CO.start3 and len(thing_list) == 2:
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


if __name__ == "__main__":
    game_loop()

pygame.quit()
quit()
