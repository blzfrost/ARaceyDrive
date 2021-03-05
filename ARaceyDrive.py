import pygame
import time
import random

pygame.init()

display_width = 600
display_height = 1000

black = (0, 0, 0)
dk_gray = (60, 60, 60)
gray = (130, 130, 130)
lt_gray = (200, 200, 200)
white = (255, 255, 255)

red = (255, 0, 0)
dk_red = (130, 0, 0)
green = (0, 255, 0)
dk_green = (0, 130, 0)
blue = (0, 0, 255)
dk_blue = (0, 0, 130)
colors = [red, dk_red, green, dk_green, blue, dk_blue]

car_width = 29
car_height = 40

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('A Racey Drive')
clock = pygame.time.Clock()

carImg = pygame.image.load('ARaceyCar.png')


class Thing:

    def __init__(self, starting_x, starting_y=-600, width=50, height=50, speed=1):
        self.x = starting_x
        self.y = starting_y
        self.width = width
        self.height = height
        self.speed = speed

    def update(self):
        dodged = False
        self.y += self.speed

        if self.y > display_height:
            self.y = -10
            dodged += 1


def things_dodged(count):
    font = pygame.font.SysFont(pygame.font.get_default_font(), 25)
    text = font.render("Dodged: " + str(count), True, black)
    gameDisplay.blit(text, (0, 0))


def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])


def car(x, y):
    gameDisplay.blit(carImg, (x, y))


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def message_display(text):
    largeText = pygame.font.SysFont(pygame.font.get_default_font(), 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    game_loop()


def crash():
    message_display('You Crashed')


def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)

    x_change = 0

    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 4
    thing_width = 100
    thing_height = 100

    # thingCount = 1

    dodged = 0

    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change
        gameDisplay.fill(white)

        # things(thingx, thingy, thingw, thingh, color)
        things(thing_startx, thing_starty, thing_width, thing_height, dk_red)

        thing_starty += thing_speed
        car(x, y)
        things_dodged(dodged)

        if x > display_width - car_width or x < 0:
            crash()

        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, display_width)
            dodged += 1
            thing_speed += 1
            thing_width += (dodged * 1.2)

        if thing_starty + 5 < y < thing_starty + thing_height - 5:
            # print('y crossover')

            if thing_startx + 5 < x < thing_startx + thing_width - 5 or thing_startx + 5 < x + car_width < thing_startx + thing_width - 5:
                # print('x crossover')
                crash()

        pygame.display.update()
        clock.tick(60)


game_loop()
pygame.quit()
quit()
