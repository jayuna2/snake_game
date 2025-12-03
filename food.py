import pygame
import random

class Food:
    def __init__(self, screen_width, screen_height, block_size=20):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.block_size = block_size
        self.spawn()

    def spawn(self):
        """Spawn food on a 20x20 grid."""
        self.x = random.randrange(0, self.screen_width, self.block_size)
        self.y = random.randrange(0, self.screen_height, self.block_size)

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), 
                         [self.x, self.y, self.block_size, self.block_size])
