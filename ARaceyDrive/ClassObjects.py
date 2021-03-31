"""
This file will hold the object data for the car, things, and data to get passed.
Not at all ready to move these out of the main file yet...
"""

import pygame
import random

# static Data
# some of these are fun to play with
high_score_file = "ARaceyDrive/high_score.txt"
display_height = 800
display_width = 500
start2 = 5  # point at which 2nt thing arrives
start3 = 15  # point at which 3rd thing arrives
starting_score = 0
starting_lives = 3
car_speed_offset = 5  # (score/car_speed_multi) + car_speed_offset
car_speed_multi = 9  # (score/car_speed_multi) + car_speed_offset
thing_speed_offset = 10  # Thing start
FPS = 60
global_multi = 0.69  # affects top speed and growth curve

# dynamic Data
score = 0
high_score = 0
lives = 0

# colors
white = (255, 255, 255)
black = (0, 0, 0)
dk_gray = (60, 60, 60)
gray = (130, 130, 130)
lt_gray = (200, 200, 200)
lt_red = (255, 100, 100)
red = (255, 0, 0)
dk_red = (130, 0, 0)
reds = [red, dk_red, lt_red]
lt_green = (100, 255, 100)
green = (0, 255, 0)
dk_green = (0, 130, 0)
greens = [green, dk_green, lt_green]
lt_blue = (100, 100, 255)
blue = (0, 0, 255)
dk_blue = (0, 0, 130)
blues = [blue, dk_blue, lt_blue]


def get_high_score():
    """Get high score from file"""
    with open(high_score_file, 'r') as hs_txt:
        return int(hs_txt.read())


def update_local_high_score_from_file():
    """Updates high score based on get_high_score"""
    global high_score
    current_hs = get_high_score()
    if current_hs is None or current_hs == "":
        pass
    elif int(current_hs) > high_score:
        high_score = int(current_hs)


def update_high_score_file():
    """Updates the high score file"""
    if high_score >= get_high_score():
        with open(high_score_file, 'w') as hs_txt:
            hs_txt.write(str(high_score))


def update_score():
    """Update score"""
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
        """Creates the car's start"""
        self.x = display_width*0.45
        self.y = display_height*0.8
        self.width = 29  # based on png, a little smaller
        self.height = 40  # based on png, a little smaller
        self.speed = car_speed_offset
        self.image = pygame.image.load("ARaceyDrive/Resources/aRaceyCar.png")
        self.left = False
        self.right = False

    # get controls to move player
    # if you forget the keyup you get a fun constant mover. Enhancement?

    def get_controls(self):
        """Get the controls from user and update the proper flags"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # Idea for alteration, single button mode.
            # 'button' will toggle direction. Horizontal movement remains active

            # Another idea, adding up and down

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
        """Updates speed to be an offset of the score"""
        self.speed = (score / car_speed_offset) + car_speed_offset

    # update player position
    def update(self):
        """Moves car based on controls"""
        self.get_controls()
        # print("Car      ", int(self.speed), " ", int(pow(self.speed, global_multi)))       # diagnose feature
        if self.left:
            self.x -= int(pow(self.speed, global_multi))
        if self.right:
            self.x += int(pow(self.speed, global_multi))

        if self.x < 0:
            self.x = 0
        if self.x > display_width - self.width:
            self.x = display_width - self.width


class Divider:
    """Lane divider logic"""
    width = int(display_width / 60)  # Need to exp with these variables
    height = int(display_height / 40)
    color = white
    speed = int(display_height / 100)

    def __init__(self, x, y):
        """Set's x and y of divider"""
        self.x = x
        self.y = y

    def reset_pos(self):
        """Returns to top of screen"""
        self.y = -1 - self.height
        # print(Divider.speed)              # diagnosis feature
        if Divider.speed < 40:
            Divider.speed += .025

    def update(self):
        """Moves divider"""
        self.y += int(self.speed)

        if self.y > display_height + 5:
            self.reset_pos()


class Thing:
    """The things that tries to "block" you
    One will be designed to grow wider
    One will grow taller
    And the last will grow both ways"""

    def __init__(self, colors=None, t_id=0, width=75, height=75):
        """Set color list and id."""
        if colors is None:
            colors = greens
        self.colors = colors
        self.id = t_id
        self.width = width     # Need to exp with these variables
        self.height = height
        self.speed = int(thing_speed_offset + self.id + score / 3)  # adds extra speed if someone starts ahead
        self.color = random.choice(self.colors)
        self.x = random.randrange(int(self.width * .25), int(display_width - self.width * .75))
        self.y = - 10 - self.height

        if self.id == 1 or self.id == 3:  # adds extra thicccness if someone starts at a higher score.
            self.width += score / 3
        if self.id == 2 or self.id == 3:
            self.height += score / 3

    def reset_pos(self):
        """Resets pos to top of screen, changes color, and updates speed"""
        self.y = int(display_height / 4 * -1) - self.height
        self.x = random.randrange(int(self.width*.25), int(display_width - self.width * .75))
        self.color = random.choice(self.colors)
        self.speed += self.id

    def reduce_numbers(self):
        """Reduces size/speed during a crash event"""
        if self.id == 1:
            self.width = (self.width + 75) / 2
        elif self.id == 2:
            self.height = (self.height + 75) / 2
        elif self.id == 3:
            self.width = (self.width + 75) / 2
            self.height = (self.height + 75) / 2

        self.speed = int((self.speed + thing_speed_offset + self.id) / 2)

    def grow(self):
        """Causes the increase of height or width based on ID"""
        if self.id == 1:
            self.width += 1
        elif self.id == 2:
            self.height += 1
        elif self.id == 3:
            self.width += 1
            self.height += 1

    def update(self, car):
        """Updates thing position, checks if below bottom of screen or overlaps with car position"""
        is_crashed = False
        # print("Thing", self.id, " ", int(self.speed), " ", int(pow(self.speed, global_multi)))  # Diagnosis
        self.y += int(pow(self.speed, global_multi))

        # checks if below screen. resets pos, increases size, increases score if it is
        if self.y > display_height + 5:
            self.reset_pos()
            if self.id < 10:
                self.grow()
                update_score()

        # checks if crash has occurred
        if self.id < 10:
            if (self.y + 5) < car.y < (self.y + self.height - 5):
                if ((self.x + 5) < car.x < (self.x + self.width - 5)) \
                        or ((self.x + 5) < car.x + car.width < (self.x + self.width - 5)):
                    is_crashed = True

        # ends with result of crash
        return is_crashed

