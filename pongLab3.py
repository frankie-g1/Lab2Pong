import pygame as pg
from ball import Ball
import random


def main():
    pg.init()

    pg.display.set_caption("My Pong")

    # Create a surface
    WIDTH = 800
    HEIGHT = 480
    BORDER = 20
    VELOCITY_x = -7
    FPS = 60
    if (bool(random.getrandbits(1)) == True):
        VELOCITY_y = -7
    else:
        VELOCITY_y = 7

    screen = pg.display.set_mode((WIDTH, HEIGHT))
    # add a solid background: r, g, b
    screen.fill((0, 0, 0))

    # double buffering: stage all changes and update them all at once
    # avoids flickering
    pg.display.update()

    # Draw walls as rectangles
    # https://www.pygame.org/docs/ref/draw.html#pygame.draw.rect
    # rect(surface, color, rect) -> Rect
    # Rect((left, top), (width, height)) -> Rect
    blackColor = pg.Color("Black")
    wcolor = pg.Color("White")
    # top wall
    pg.draw.rect(screen, wcolor, pg.Rect((0, 0), (WIDTH, BORDER)))
    # left wall
    pg.draw.rect(screen, wcolor, pg.Rect((0, 0), (BORDER, HEIGHT)))
    # bottom wall
    pg.draw.rect(screen, wcolor, pg.Rect((0, HEIGHT - BORDER), (WIDTH, BORDER)))
    # no right wall
    # pg.draw.rect(screen, wcolor, pg.Rect((0,HEIGHT), (BORDER, WIDTH)))

    # Ball init
    x0 = WIDTH - Ball.RADIUS
    y0 = HEIGHT // 2
    vx0 = VELOCITY_x
    vy0 = VELOCITY_y
    wall = BORDER
    ceiling = BORDER
    floor = HEIGHT - BORDER
    ycolor = pg.Color("Yellow")
    # Todo: +/- 45 degree random
    a = Ball(x0, y0, vx0, vy0, ycolor, blackColor, screen, wall, ceiling, floor)

    pg.display.update()

    # define a variable to control the main loop
    running = True
    clock = pg.time.Clock()

    # main loop
    while running:
        # event handling, gets all event from the event queue (POLLING)
        # Event is a queue
        for event in pg.event.get():
            # only do something if the event is of TYPE QUIT
            if event.type == pg.QUIT:
                # change value to false, to exit the main loop
                running = False
        a.update()
        pg.display.update()
        clock.tick(FPS)


if __name__ == "__main__":
    # call the main function
    main()
