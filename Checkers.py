import os
import pygame
from Tile import Tile


class Checkers:
    def __init__(self):
        self.CONST_tile_side_length = 100
        self.screen = None
        self.running = True
        self.tiles = [
            [Tile(x * self.CONST_tile_side_length,
                  y * self.CONST_tile_side_length,
                  self.CONST_tile_side_length,
                  Tile.get_bgcolor(x, y))
             for y in range(8)
             ]
            for x in range(8)
        ]
        self.tile_images = pygame.sprite.Group()

        for y in self.tiles:
            for x in y:
                self.tile_images.add(x.sprite)

        self.pygame_init()

    def check_pygame_events(self):
        for e in pygame.event.get():
            if e.type == pygame.QUIT or (e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE):
                self.running = False
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_r:
                    self.reset_game()

    def draw(self):
        self.tile_images.draw(self.screen)
        pygame.display.flip()

    def pygame_init(self):
        os.environ["SDL_VIDEO_CENTERED"] = "1"
        pygame.init()

        self.screen = pygame.display.set_mode((8 * self.CONST_tile_side_length, 8 * self.CONST_tile_side_length))

    def run(self):
        while self.running:
            self.check_pygame_events()
            self.run_game_logic()
            self.draw()

    def reset_game(self):
        pass

    def run_game_logic(self):
        pass

