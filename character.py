import pygame

def snake_head(window):
    head_size=[x_head, y_head, head_width, head_height]
    head= pygame.draw.rect(window, snake_colour, head_size, 0)
    return head

def snake_body(window):
    body_size= [x_body, y_body, body_width, body_height]
    body= pygame.draw.rect(window, snake_colour, body_size, 0 )
    return body


head_size=[400,250,14,18] #x, y, width, height
snake_colour =(135, 206, 235) #RGB
x_head,y_head, head_width, head_height = head_size

body_width = head_width
body_height= head_height -4
x_body= x_head- body_width
y_body = y_head +2



def movement(window, events):
    snake= snake_head(window), snake_body(window)
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                global x_head
                global x_body
                x_head +=10
                x_body +=10
            if event.key == pygame.K_LEFT:
             
               
                new_x_head= x_body
                new_x_body =x_head
                
                x_head = new_x_head-10
                x_body = new_x_body
