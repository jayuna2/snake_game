import pygame


head_size = [400, 250, 20, 20]
x_head, y_head, head_width, head_height = head_size


body_width = 20
body_height = 20
x_body = x_head - 20
y_body = y_head

current_direction = 'RIGHT'
change_direction = 20  


snake_parts = [
    [x_head, y_head, head_width, head_height],
    [x_body, y_body, body_width, body_height]
]

def snake_drawing(window):
    head_color = (81, 123, 204)
    body_color = (105, 163, 225)

    
    pygame.draw.rect(window, head_color, snake_parts[0], 0)

    
    for part in snake_parts[1:]:
        pygame.draw.rect(window, body_color, part, 0)

def snake_position():
    """Move the snake by inserting a new head and removing the last part."""
    global snake_parts, current_direction

    new_head = snake_parts[0].copy()

    if current_direction == 'RIGHT':
        new_head[0] += change_direction
    elif current_direction == 'LEFT':
        new_head[0] -= change_direction
    elif current_direction == 'UP':
        new_head[1] -= change_direction
    elif current_direction == 'DOWN':
        new_head[1] += change_direction

    snake_parts.insert(0, new_head)
    snake_parts.pop()

def user_input(events):
    global current_direction

    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and current_direction != 'LEFT':
                current_direction = 'RIGHT'
            elif event.key == pygame.K_LEFT and current_direction != 'RIGHT':
                current_direction = 'LEFT'
            elif event.key == pygame.K_UP and current_direction != 'DOWN':
                current_direction = 'UP'
            elif event.key == pygame.K_DOWN and current_direction != 'UP':
                current_direction = 'DOWN'

def check(screen_size):
    """Return True if snake hits wall or its own body."""
    width, height = screen_size
    head_x = snake_parts[0][0]
    head_y = snake_parts[0][1]

    
    if head_x < 0 or head_x >= width:
        return True
    if head_y < 0 or head_y >= height:
        return True

    
    for part in snake_parts[1:]:  
        if head_x == part[0] and head_y == part[1]:
            return True

    return False
