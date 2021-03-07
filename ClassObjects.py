"""
This file will hold the object data for the car, things, and data to get passed.
Not at all ready to move these out of the main file yet...
"""

import pygame
import random

""""The answer is yes!"""

# Static Data
display_height = 1000
display_width = 600

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

# Dynamic Data
score = 0
high_score = 0  # Will need to figure out how to implement
global_multi = 0.5


def update_score():
    global score
    score += 1


class Thing:
    """The things that "block" you
    One will be designed to grow wider
    One will grow taller
    And the last will grow both ways"""
    def __init__(self, colors, t_id):
        self.colors = colors
        self.id = t_id
        self.width = 50
        self.height = 50
        self.speed = 1
        # self.passes = 0 # Might use to alter the speed variable
        self.color = random.choice(colors)
        self.x = random.randrange(int(self.width * .25), int(display_width - self.width * .75))
        self.y = -600

    def reset_pos(self):
        self.y = -5 - self.height
        self.x = random.randrange(int(self.width*.25), int(display_width - self.width * .75))
        self.color = random.choice(self.colors)
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
        crash = False
        self.y += pow(self.speed, global_multi)

        if self.y > display_height + 5:
            self.reset_pos()
            self.grow()
            update_score()

        if (self.y + 5) < car.y < (self.y + self.height - 5):
            print("Y crossover")
            if ((self.x + 5) < car.x < (self.x + self.width - 5)) \
                    or ((self.x + 5) < car.x + car.width < (self.x + self.width - 5)):
                crash = True
                print("Crash")

        return crash


class Car:
    """The car object the player controls"""
    def __init__(self):
        self.x = display_width*0.45
        self.y = display_height*0.8
        self.width = 29
        self.height = 40
        self.speed = 5
        self.image = pygame.image.load("ARaceyCar.png")
        self.left = False
        self.right = False

    def get_controls(self):
        for event in pygame.event.get():
            if event.type == pygame.quit():
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_Left or event.key == pygame.K_a:
                    self.left = True
                    self.right = False
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    self.left = False
                    self.right = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.left = False
                if event.key == pygame.K_RIGHT:
                    self.right = False

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
