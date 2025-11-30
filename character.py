import pygame

head_size=[400,250,16,16] #x, y, width, height

x_head,y_head, head_width, head_height = head_size

body_width = head_width
body_height= head_height -4
x_body= x_head
y_body = y_head

current_direction ='RIGHT' #initial position of the snake 
change_direction = 15

snake_parts =[
    [x_head, y_head, head_width, head_height],
    [x_body, y_body, body_width, body_height]
]

def snake_drawing(window):
    global snake_parts
    body_colour =(105, 163, 225) #RGB
    head_colour= (81, 123, 204)

    if snake_parts:
        head_part = snake_parts[0]
        pygame.draw.rect(window, head_colour, head_part, 0)

        for i in range (1, len(snake_parts)):
            body_part = snake_parts[i]
            pygame.draw.rect(window, body_colour, body_part, 0)


def snake_position():
    global snake_parts, current_direction

    new_head = snake_parts[0].copy()

    if current_direction =='RIGHT':
        new_head[0] += change_direction
    elif current_direction =='LEFT':
        new_head[0] -= change_direction
    elif current_direction =='UP':
        new_head[1] -= change_direction
    elif current_direction == 'DOWN':
        new_head[1] += change_direction

    snake_parts.insert(0, new_head)
    snake_parts.pop()

def user_input(events):
    global current_direction

    for event in events:
        if event.type==pygame.KEYDOWN:
            new_direction =current_direction

            if event.key == pygame.K_RIGHT:
                if current_direction != 'LEFT':
                    new_direction = 'RIGHT'
            elif event.key == pygame.K_LEFT:
                if current_direction != 'RIGHT':
                    new_direction = 'LEFT'
            elif event.key == pygame.K_UP:
                if current_direction!='DOWN':
                    new_direction = 'UP'
            elif event.key == pygame.K_DOWN:
                if current_direction != 'UP':
                    new_direction = 'DOWN'
            
            current_direction = new_direction


def check (screen_size):
    screen_width= screen_size[0]
    screen_height = screen_size[1]
    global snake_parts

    head_x_position = snake_parts[0][0]
    head_y_position = snake_parts [0][1]

    if not snake_parts:
        return False
    
    if head_x_position<0 or head_x_position > screen_width:
        return True
    
    if head_y_position<0 or head_y_position > screen_height:
        return True
    
    return False



