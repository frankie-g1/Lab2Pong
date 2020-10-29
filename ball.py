import pygame


class Ball:
    RADIUS = 10

    def __init__(self, x, y, vx, vy, fgcolor, bgcolor, screen, wall, ceiling, floor):
        # Instance variables
        self.x = x
        self.y = y
        self.screen = screen
        self.vx = vx
        self.vy = vy
        self.fgcolor = fgcolor
        self.bgcolor = bgcolor
        self.wall = wall + self.RADIUS
        self.ceiling = ceiling + self.RADIUS
        self.floor = floor - self.RADIUS

    def show(self, color):
        pygame.draw.circle(self.screen, color, (self.x, self.y), self.RADIUS)

    def update(self):
        # Todo:
        # Check if I'm colliding with wall position:
        # Flip the direction
        if self.x <= self.wall + self.RADIUS:
            self.vx = -1 * self.vx
        elif self.y <= self.ceiling + self.RADIUS or self.y >= self.floor - self.RADIUS:
            self.vy = -1 * self.vy

        # new position = old position + delta position
        # delta position = velocity
        # delete the old ball
        self.show(self.bgcolor)
        self.x = self.x + self.vx
        self.y = self.y + self.vy

        self.show(self.fgcolor)
