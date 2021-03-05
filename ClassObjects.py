"""
This file will hold the object data for the car, things, and data to get passed.
Not at all ready to move these out of the main file yet...
"""

import pygame


class CoreData:
    """Trying to see if I can use this to pass certain data better
    May explode in my face!"""
    def __init__(self, display_width=600, display_height=1000):
        self.display_width = display_width
        self.display_height = display_height

    class Colors:
        red = (255, 0, 0)
        dk_red = (130, 0, 0)
        green = (0, 255, 0)
        dk_green = (0, 130, 0)
        blue = (0, 0, 255)
        dk_blue = (0, 0, 130)
        colors = [red, dk_red, green, dk_green, blue, dk_blue]

# Testing concept
# It works
# test_thing = CoreData
# print(test_thing.Colors.red)


class Thing:

    def __init__(self, color, starting_x, starting_y=-600, width=50, height=50, speed=1):
        self.x = starting_x
        self.y = starting_y
        self.width = width
        self.height = height
        self.speed = speed
        self.color = color

    def update(self, display_height):
        dodged = False
        self.y += self.speed

        if self.y > display_height:  # Found a hurdle... Gonna need to figure out how to pass this properly.
            self.y = -10
            dodged += 1


class Car:
    """Need to work on encapsulating the movement into an update method."""
    def __init__(self, starting_x, starting_y, width, height, speed):
        self.x = starting_x
        self.y = starting_y
        self.x_change = 0
        self.width = width
        self.height = height
        self.speed = speed

    def get_controls(self):
        for event in pygame.event.get():
            if event.type == pygame.quit():
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_Left or event.key == pygame.K_a:
                    self.x_change = -5
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    self.x_change = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
