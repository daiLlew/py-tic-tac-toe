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
NAUGHT = "o"
CROSS = "x"


def main():
    pygame.init()
    global FPSCLOCK, DISPLAYSURF

    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE), 0, 32)
    pygame.display.set_caption(TITLE)

    # create a new game board
    board = Board()
    user = Player(CROSS, "user")
    computer = Player(NAUGHT, "computer")
    current_player = user

    while True:
        for event in pygame.event.get():
            checkForExit(event)

            if event.type == MOUSEMOTION:
                mouse_x, mouse_y = event.pos
                board.highlight_under_mouse(mouse_x, mouse_y)

            if event.type == MOUSEBUTTONDOWN:
                if board.clicked(current_player, mouse_x, mouse_y):
                    if current_player == user:
                        current_player = computer
                    else:
                        current_player = user

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

    def highlight_under_mouse(self, mouse_x, mouse_y):
        for tile in self.tiles:
            if tile.rect.collidepoint(mouse_x, mouse_y):
                tile.highlighted = True
            else:
                tile.highlighted = False

    def clicked(self, player, mouseX, mouseY):
        for i in range(0, len(self.tiles)):
            t = self.tiles[i]
            if t.rect.collidepoint(mouseX, mouseY):
                return t.set_symbol(player)
        return False

    def draw(self):
        DISPLAYSURF.fill(GREY)

        for tile in self.tiles:
            tile.draw()


class Tile:
    value = None
    highlighted = False
    rect = None
    highlightRect = None
    symbol = None

    def __init__(self, xco, yco):
        self.value = None
        self.symbol = None
        self.rect = pygame.Rect(xco, yco, TILE_SIZE, TILE_SIZE)

        x = self.rect.topleft[0] - 5
        y = self.rect.topleft[1] - 5
        self.highlightRect = pygame.Rect(x, y, HIGHLIGHT_SIZE, HIGHLIGHT_SIZE)

    def set_symbol(self, player):
        if self.symbol is None:
            self.symbol = Symbol(player.symbol, self)
            return True

        return False

    def is_empty(self):
        return self.value is None

    def is_highlighted(self):
        return self.highlighted

    def set_value(self, value):
        self.value = value

    def draw(self):
        # draw the highlight around the tile if the mouse is over it.
        if self.highlighted:
            pygame.draw.rect(DISPLAYSURF, WHITE, self.highlightRect)

        # draw the tile background
        pygame.draw.rect(DISPLAYSURF, BLACK, self.rect)

        if self.symbol is not None:
            DISPLAYSURF.blit(self.symbol.text, self.symbol.text_rect)


class Symbol:
    text = None
    text_rect = None

    def __init__(self, value, tile):
        self.basicFont = pygame.font.SysFont(None, 250)
        self.text = self.basicFont.render(value, True, WHITE, None)
        self.text_rect = self.text.get_rect()
        self.text_rect.centerx = tile.rect.centerx
        self.text_rect.centery = tile.rect.centery


if __name__ == '__main__':
    main()
