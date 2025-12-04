import pygame

pygame.font.init()
score_font = pygame.font.SysFont("arial", 25)
game_over_font = pygame.font.SysFont("arial", 40)
instruction_font = pygame.font.SysFont("arial", 40)
help_font = pygame.font.SysFont("arial", 25)

def show_score(screen, score):
    text = score_font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(text, (10, 10))

def game_over_screen(screen, width, height):
    game_over_text = game_over_font.render("GAME OVER", True, (255, 0, 0))
    restart_text = score_font.render("Press R to Restart", True, (255, 255, 255))
    screen.blit(game_over_text, (width // 3, height // 3))
    screen.blit(restart_text, (width // 3.2, height // 2))

def start_text(screen):
    width, height = screen.get_size()
    instruction_text = instruction_font.render("Press Any key to start ", True, (255, 0, 0))
    screen.blit(instruction_text, (width//2, height//2))

def help(screen):
    width, height = screen.get_size()
    help_text = help_font.render("Help ", True, (255, 255, 255))

    help_rect = help_text.get_rect()
    help_rect.topleft = (110, 10)

    screen.blit(help_text, help_rect)

    return help_rect

    