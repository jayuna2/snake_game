import pygame

pygame.font.init()
score_font = pygame.font.SysFont("arial", 25)
game_over_font = pygame.font.SysFont("arial", 40)

def show_score(screen, score):
    text = score_font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(text, (10, 10))

def game_over_screen(screen, width, height):
    game_over_text = game_over_font.render("GAME OVER", True, (255, 0, 0))
    restart_text = score_font.render("Press R to Restart", True, (255, 255, 255))
    screen.blit(game_over_text, (width // 3, height // 3))
    screen.blit(restart_text, (width // 3.2, height // 2))
