class Thing:

    def __init__(self, starting_x, starting_y=-600, width=50, height=50, speed=1):
        self.x = starting_x
        self.y = starting_y
        self.width = width
        self.height = height
        self.speed = speed

    def update(self, display_height):
        dodged = False
        self.y += self.speed

        if self.y > display_height:
            self.y = -10
            dodged = True

        if dodged