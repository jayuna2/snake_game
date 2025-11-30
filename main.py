import pygame
import character


def main_screen():
    pygame.init()
    size = (800,500)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Snake Game')
    return screen

def game_loop():
    start = True
    window = main_screen()
    while start:
        events= pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                start = False
        
        character.snake_drawing(window)
        pygame.display.update()
        window.fill((0,0,0))
        


game_loop()