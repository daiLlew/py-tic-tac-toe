import sys

import pygame
from pygame.locals import *

FPS = 30

# Colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
GREY = (125, 125, 125)

# Display object dimensions and vars
TITLE = "Tic-tac-toe"
SCREEN_SIZE = 490
MARGIN = 10
TILE_SIZE = 150


def main():
    global FPSCLOCK, DISPLAYSURF

    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE), 0, 32)
    pygame.display.set_caption(TITLE)

    pygame.init()

    tile_coords = get_tile_coords()
    for i in range(0, 3):
        print(tile_coords[i], tile_coords[i + 1], tile_coords[i + 2])
        i += 3

    highlighTile = None

    while True:
        for event in pygame.event.get():
            checkForExit(event)

            if event.type == MOUSEMOTION:
                mousex, mousey = event.pos
                highlighTile = highlight_title(mousex, mousey, tile_coords)

        DISPLAYSURF.fill(BLACK)

        draw(tile_coords, highlighTile)
        pygame.display.update()
        FPSCLOCK.tick(FPS)


def checkForExit(event):
    if event.type == QUIT:
        print("exiting py-tic-tac-toe")
        pygame.quit()
        sys.exit()


def highlight_title(mousex, mousey, tile_coords):
    for tile in tile_coords:
        t = pygame.Rect(tile[0], tile[1], TILE_SIZE, TILE_SIZE)

        if t.collidepoint(mousex, mousey):
            return t
    return None


def get_tile_coords():
    tile_coordinates = []
    xco = 0
    yco = MARGIN

    for y in range(0, 3):
        for x in range(0, 3):
            xco += MARGIN
            tile_coordinates.append((xco, yco))
            xco += TILE_SIZE

        xco = 0
        yco += TILE_SIZE + MARGIN

    return tile_coordinates


def draw(coords, highlighTile):
    for t in coords:
        pygame.draw.rect(DISPLAYSURF, GREY, (t[0], t[1], TILE_SIZE, TILE_SIZE))

    if highlighTile:
        pygame.draw.rect(DISPLAYSURF, WHITE, highlighTile)


if __name__ == '__main__':
    main()
