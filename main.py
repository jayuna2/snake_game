import pygame
import character
from food import Food
import ui

def main_screen():
    pygame.init()
    screen = pygame.display.set_mode((800, 500))
    pygame.display.set_caption("Snake Game")
    return screen

def game_loop():
    window = main_screen()
    width, height = window.get_size()

    food = Food(width, height, 20)
    score = 0
    game_over = False

    clock = pygame.time.Clock()
    SPEED = 8

    running = True
    while running:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False
            
            if event.type ==pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    character.restart(events)

            if game_over and event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                return game_loop()  

        if not game_over:
            character.user_input(events)
            character.snake_position()

        
        head_x = character.snake_parts[0][0]
        head_y = character.snake_parts[0][1]

        
        snake_rect = pygame.Rect(head_x, head_y, 20, 20)
        food_rect = pygame.Rect(food.x, food.y, food.block_size, food.block_size)

        if snake_rect.colliderect(food_rect):
            score += 1
            food.spawn()
            character.snake_parts.append(character.snake_parts[-1].copy())

        
        if character.check((width, height)):
            game_over = True

        background = pygame.image.load("photo/Untitled1design.png")
        window.blit(background, (0,0))
        
        character.snake_drawing(window)
        food.draw(window)
        ui.show_score(window, score)

        if game_over:
            ui.game_over_screen(window, width, height)

        pygame.display.update()
        clock.tick(SPEED)

    pygame.quit()

game_loop()
