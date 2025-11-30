import pygame

head_size=[400,250,14,18] #x, y, width, height
snake_colour =(135, 206, 235) #RGB
x_head,y_head, head_width, head_height = head_size

body_width = head_width
body_height= head_height -4
x_body= x_head- body_width
y_body = y_head +2

current_direction= 'RIGHT' #initial direction of snake
snake_speed = 10

snake_parts =[
    [x_head, y_head, head_width, head_height],
    [x_body, y_body, body_width, body_height]
]

def snake_drawing(window):
    global snake_parts

    for part in snake_parts:
        pygame.draw.rect(window, snake_colour, part, 0)


