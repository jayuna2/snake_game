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
    game_over = False
    window = main_screen()
    screen_size = window.get_size()

    clock =pygame.time.Clock()
    SPEED = 8
    while start:
        events= pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                start = False

        if not game_over:    
            character.user_input(events)
            character.snake_position()

        if character.check(screen_size):
            game_over = True

        window.fill((0,0,0))
        character.snake_drawing(window)
        pygame.display.update()
        clock.tick(SPEED)

    pygame.quit()

game_loop()