"""
This file will hold the object data for the car, things, and data to get passed.
Not at all ready to move these out of the main file yet...
"""

import pygame
import random

# Static Data
display_height = 1000
display_width = 600
start2 = 10
start3 = 20

# Dynamic Data
score = 0
high_score = 0  # Will need to figure out how to implement
global_multi = 0.8
FPS = 60
lives = 3

# Colors
black = (0, 0, 0)
dk_gray = (60, 60, 60)
gray = (130, 130, 130)
lt_gray = (200, 200, 200)
white = (255, 255, 255)
red = (255, 0, 0)
dk_red = (130, 0, 0)
reds = [red, dk_red]
green = (0, 255, 0)
dk_green = (0, 130, 0)
greens = [green, dk_green]
blue = (0, 0, 255)
dk_blue = (0, 0, 130)
blues = [blue, dk_blue]


def update_score():
    global score
    global high_score
    score += 1

    # update high score
    if score > high_score:
        high_score = score


class Car:
    """The car object the player controls"""
    def __init__(self):
        self.x = display_width*0.45
        self.y = display_height*0.8
        self.width = 29
        self.height = 40
        self.speed = 5
        self.image = pygame.image.load("aRaceyCar.png")
        self.left = False
        self.right = False

    def get_controls(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    self.left = True
                    self.right = False
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    self.left = False
                    self.right = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    self.left = False
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    self.right = False

    def upgrade(self):
        self.speed += 1

    def update(self):
        self.get_controls()
        if self.left:
            self.x -= pow(self.speed, global_multi)
        if self.right:
            self.x += pow(self.speed, global_multi)

        if self.x < 0:
            self.x = 0
        if self.x > display_width - self.width:
            self.x = display_width - self.width

        # game_display.blit(self.image, (self.x, self.y))


class Thing:
    """The things that "block" you
    One will be designed to grow wider
    One will grow taller
    And the last will grow both ways"""
    # I wonder how to repurpose this to make the lane dividers
    def __init__(self, colors, t_id, x=0, y=0, width=75, height=75):
        self.colors = colors
        self.id = t_id
        self.width = width     # Need to exp with these variables
        self.height = height
        self.speed = 10
        # self.passes = 0 # Might use to alter the speed variable
        self.color = random.choice(self.colors)
        if self.id < 10:
            self.x = random.randrange(int(self.width * .25), int(display_width - self.width * .75))
            self.y = - 10 - self.height
        else:
            self.x = x
            self.y = y

    def reset_pos(self):
        self.y = ((self.id * 5) * -1) - self.height
        if self.id < 10:
            self.x = random.randrange(int(self.width*.25), int(display_width - self.width * .75))
        self.color = random.choice(self.colors)
        # need a better way to update score
        # self.speed += 1
        # self.speed = score / 3
        # self.speed = 10 + (score / 3 * self.id)
        # self.speed = 10 + (score / 3 + pow(self.id, self.id))
        if self.id < 10:
            self.speed += self.id
        else:
            self.speed += 1

    def grow(self):
        if self.id == 1:
            self.width += 1
        elif self.id == 2:
            self.height += 1
        elif self.id == 3:
            self.width += 1
            self.height += 1

    def update(self, car):
        is_crashed = False
        if self.id < 10:
            self.y += pow(self.speed, global_multi)
        else:
            self.y += self.speed * global_multi

        if self.y > display_height + 5:
            self.reset_pos()
            if self.id < 10:
                self.grow()
                update_score()

        if self.id < 10:
            if (self.y + 5) < car.y < (self.y + self.height - 5):
                print("Y crossover")
                if ((self.x + 5) < car.x < (self.x + self.width - 5)) \
                        or ((self.x + 5) < car.x + car.width < (self.x + self.width - 5)):
                    is_crashed = True
                    print("Crash")

        return is_crashed

