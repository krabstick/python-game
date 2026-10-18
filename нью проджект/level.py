import pygame
from settings import TILE

game_map = [[1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 1, 0, 1, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 1, 0, 1, 1, 0, 1],
            [1, 0, 1, 1, 0, 1, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 1, 0, 1, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1]]

def get_coins():
    coins = [pygame.Rect(TILE * 2 + 15, TILE * 1 + 15, 10, 10),
             pygame.Rect(TILE * 4 + 15, TILE * 1 + 15, 10, 10),
             pygame.Rect(TILE * 2 + 15, TILE * 3 + 15, 10, 10)]
    score = 0

def build_walls() -> list:
    walls = []
    for row_index, row in enumerate(game_map):
        for col_index, cell in enumerate(row):
            if cell == 1:
                x = col_index * TILE
                y = row_index * TILE
                walls.append(pygame.Rect(x, y, TILE, TILE))
    return walls