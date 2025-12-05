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

    background = pygame.image.load("photo/background.png")
    help_image = pygame.image.load("photo/help.png")

    running = True
    start = False # to display starting text
    show_help = False
    while running:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False
            
            if event.type ==pygame.KEYDOWN:
                start = True
                if event.key == pygame.K_r:
                    character.restart(events)
            
            if game_over and event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                return game_loop()  
            
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_pos = event.pos

                if ui.help(window).collidepoint(mouse_pos):
                    show_help = not show_help
            
        
        window.blit(background, (0,0))

        
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


        character.snake_drawing(window)
        ui.show_score(window, score)
        

        if not game_over and start:
            food.draw(window)
            character.user_input(events)
            character.snake_position()
            

        elif not start:
            ui.start_text(window) 

        if game_over:
            ui.game_over_screen(window, width, height)

        if show_help:
             window.blit(help_image, (0,0))
        
        ui.help(window) 

        pygame.display.update()
        clock.tick(SPEED)

    pygame.quit()

game_loop()
