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
HIGHLIGHT_SIZE = TILE_SIZE + 10


def main():
    global FPSCLOCK, DISPLAYSURF

    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE), 0, 32)
    pygame.display.set_caption(TITLE)

    pygame.init()

    # create a new game board
    board = Board()

    while True:
        for event in pygame.event.get():
            checkForExit(event)

            if event.type == MOUSEMOTION:
                mouseX, mouseY = event.pos
                board.highlight_under_mouse(mouseX, mouseY)

            if event.type == MOUSEBUTTONDOWN:
                clickedIndex = board.get_clicked(mouseX, mouseY)
                if clickedIndex > -1:
                    print("tile ", clickedIndex, " was clicked")


        board.draw()

        pygame.display.update()
        FPSCLOCK.tick(FPS)


# Check and handle a quit event
def checkForExit(event):
    if event.type == QUIT:
        print("exiting py-tic-tac-toe")
        pygame.quit()
        sys.exit()


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


class Player:
    symbol = ""
    name = ""

    def __init__(self, symbol, name):
        self.symbol = symbol
        self.name = name


class Board:
    tiles = []

    def __init__(self):
        self.tiles = []
        coords = get_tile_coords()
        for i in range(0, 9):
            self.tiles.append(Tile(coords[i][0], coords[i][1]))

    def get_tile(self, index):
        return self.tiles[index]

    def highlight_under_mouse(self, mouseX, mouseY):
        for tile in self.tiles:
            if tile.Rect.collidepoint(mouseX, mouseY):
                tile.highlighted = True
            else:
                tile.highlighted = False

    def get_clicked(self, mouseX, mouseY):
        for i in range(0, len(self.tiles)):
            t = self.tiles[i]
            if t.Rect.collidepoint(mouseX, mouseY):
                return i
        return -1

    def draw(self):
        DISPLAYSURF.fill(BLACK)

        for tile in self.tiles:
            if tile.highlighted:
                pygame.draw.rect(DISPLAYSURF, WHITE, tile.highlightRect)

            pygame.draw.rect(DISPLAYSURF, GREY, tile.Rect)


class Tile:
    value = None
    highlighted = False
    Rect = None
    highlightRect = None

    def __init__(self, xco, yco):
        self.value = None
        self.Rect = pygame.Rect(xco, yco, TILE_SIZE, TILE_SIZE)
        self.highlightRect = pygame.Rect(self.Rect.topleft[0] - 5, self.Rect.topleft[1] - 5, HIGHLIGHT_SIZE,
                                         HIGHLIGHT_SIZE)

    def is_empty(self):
        return self.value is None

    def is_highlighted(self):
        return self.highlighted

    def set_value(self, value):
        self.value = value


if __name__ == '__main__':
    main()
