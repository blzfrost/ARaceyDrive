"""
This file will hold the object data for the car, things, and data to get passed.
Not at all ready to move these out of the main file yet...
"""

import pygame
import random

# static Data
display_height = 1000
display_width = 600
start2 = 5  # bringing in sooner
start3 = 15  # bringing in sooner
high_score_file = "high_score.txt"

# dynamic Data
score = 0
high_score = 0
global_multi = 0.67
FPS = 60
lives = 3

# colors
white = (255, 255, 255)
black = (0, 0, 0)
dk_gray = (60, 60, 60)
gray = (130, 130, 130)
lt_gray = (200, 200, 200)
red = (255, 0, 0)
dk_red = (130, 0, 0)
reds = [red, dk_red]
green = (0, 255, 0)
dk_green = (0, 130, 0)
greens = [green, dk_green]
blue = (0, 0, 255)
dk_blue = (0, 0, 130)
blues = [blue, dk_blue]


def get_high_score():
    """get high score from file"""
    with open(high_score_file, 'r') as hs_txt:
        return int(hs_txt.read())


def update_local_high_score_from_file():
    global high_score
    current_hs = get_high_score()
    if current_hs is None or current_hs == "":
        pass
    elif int(current_hs) > high_score:
        high_score = int(current_hs)


def update_high_score_file():
    # global high_score
    if high_score >= get_high_score():
        with open(high_score_file, 'w') as hs_txt:
            hs_txt.write(str(high_score))


def update_score():
    """update score"""
    global score
    global high_score
    score += 1

    # update high score
    if score > high_score:
        high_score = score
        update_high_score_file()


class Car:
    """the car object the player controls"""
    def __init__(self):
        self.x = display_width*0.45
        self.y = display_height*0.8
        self.width = 29
        self.height = 40
        self.speed = 5
        self.image = pygame.image.load("aRaceyCar.png")
        self.left = False
        self.right = False

    # get controls to move player
    # if you forget the keyup you get a fun constant mover. Enhancement?
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

    # command to update speed
    def upgrade(self):
        self.speed += 1

    # update player position
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


class Divider:
    """Lane divider logic"""
    width = 10  # Need to exp with these variables
    height = 40
    color = white
    speed = 10

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def reset_pos(self):
        self.y = -1 - self.height
        if Divider.speed < 40:
            Divider.speed += .01

    def update(self):
        self.y += int(self.speed)
        # print(Divider.speed)

        if self.y > display_height + 5:
            self.reset_pos()


class Thing:
    """The things that "block" you
    One will be designed to grow wider
    One will grow taller
    And the last will grow both ways"""
    def __init__(self, colors, t_id, x=0, y=0, width=75, height=75):
        self.colors = colors
        self.id = t_id
        self.width = width     # Need to exp with these variables
        self.height = height
        self.speed = 10 + self.id
        # self.passes = 0 # Might use to alter the speed variable
        self.color = random.choice(self.colors)
        if self.id < 10:
            self.x = random.randrange(int(self.width * .25), int(display_width - self.width * .75))
            self.y = - 10 - self.height
        else:
            self.x = x
            self.y = y

    def reset_pos(self):
        self.y = -1 - self.height  # ((self.id * 5) * -1) - self.height
        if self.id < 10:
            self.x = random.randrange(int(self.width*.25), int(display_width - self.width * .75))
        self.color = random.choice(self.colors)
        if self.id < 10:
            self.speed += self.id
        else:
            self.speed += .3

    def reduce_numbers(self):
        """Reduces size/speed during a crash event"""
        if self.id == 1:
            self.x /= 2
            if self.x < 75:
                self.x = 75
        elif self.id == 2:
            self.y /= 2
            if self.y < 75:
                self.y = 75
        elif self.id == 3:
            self.x /= 2
            if self.x < 75:
                self.x = 75
            self.y /= 2
            if self.y < 75:
                self.y = 75

        self.speed = self.speed / 2
        if self.speed < 10 + self.id:
            self.speed = 10 + self.id

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
            self.y += int(pow(self.speed, global_multi))
        else:
            self.y += int(self.speed * global_multi)

        if self.y > display_height + 5:
            self.reset_pos()
            if self.id < 10:
                self.grow()
                update_score()

        if self.id < 10:
            if (self.y + 5) < car.y < (self.y + self.height - 5):
                # print("Y crossover")
                if ((self.x + 5) < car.x < (self.x + self.width - 5)) \
                        or ((self.x + 5) < car.x + car.width < (self.x + self.width - 5)):
                    is_crashed = True
                    # print("Crash")

        return is_crashed

