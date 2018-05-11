import pygame
from Piece import Piece

class Tile:
    def __init__(self, x_pos, y_pos, side_length, bgcolor):
        self.sprite = TileSprite(self)
        self.sprite.image = pygame.Surface([side_length, side_length])
        self.sprite.rect = pygame.Rect(x_pos, y_pos, side_length, side_length)
        self.sprite.image.fill(0x444444)
        self.bgcolor = bgcolor
        pygame.draw.rect(self.sprite.image, self.bgcolor, pygame.Rect(1, 1, side_length - 2, side_length - 2))
        self.contents = Piece(None)

    @staticmethod
    def get_bgcolor(x, y):
        if x % 2 == y % 2:
            return 0xff0000
        else:
            return 0x000000


class TileSprite(pygame.sprite.Sprite):
    def __init__(self, parent):
        super(TileSprite, self).__init__()
        self.parent = parent
