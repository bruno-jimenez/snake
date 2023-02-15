from tkinter import *
import pygame
import random
from pygame import event
import time

#[---------------------------------]
# creating the window and setup 
#[---------------------------------]

pygame.init()
pygame.font.init()
speed = 15
fps = pygame.time.Clock()

# window setup
root = Tk()
root.title("Snake")
x = 500
y = 400
window = pygame.display.set_mode((x, y))
pygame.display.set_caption("Snake")
font = pygame.font.Font(None, 35)

# color setup
green = pygame.Color(0, 255, 0)
black = pygame.Color(0, 0, 0)
red = pygame.Color(255, 0, 0)
white = pygame.Color(255, 255, 255)

#spawn creation
body = [[100, 50], [90, 50], [80, 50], [70, 50]]
position = [100, 50]
direction = 'RIGHT'
change_to = direction

# Condition for the global loop
Running = True
score = 0
score_increment = 1
last_score = ''

# Return a random number for spawn a fruit into the screen
x=400
y=500
fruit_spawn = False
fruit = [random.randrange(1, (x//10))*10, random.randrange(1, (y//10))*10]

# Create the physical form of the snake and fruits
for pos in body:
    pygame.draw.rect(window, green, pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(window, red, pygame.Rect(fruit[0], fruit[1], 10, 10))

#[---------------------------------]
#    creating the loop
#[---------------------------------]

def global_loop():
    global Running
    global direction
    global change_to
    global body
    global position
    global last_score
    global score

while Running:
        for event in pygame.event.get():

            # Quit the program if close button is clicked
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

#[---------------------------------]
#    fonction for feeding snake
#[---------------------------------]

        def feeding():
            if position[0] == fruit[0] and position[1] == fruit[1]:
                fruit_spawn = False
                score += score_increment
            else:
                body.pop()        
        



#[---------------------------------]
#      spawn & respawn apple
#[---------------------------------]

        def apple_generator():
            if not fruit_spawn:
                fruit = [random.randrange(1, (x // 10)) * 10, random.randrange(1, (y // 10)) * 10]
            fruit_spawn = True
        

#[---------------------------------]
#  fonction for bind arrow key
#[---------------------------------]

        def binding():
    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    change_to = 'LEFT'
                if event.key == pygame.K_UP:
                    change_to = 'UP'
                if event.key == pygame.K_RIGHT:
                    change_to = 'RIGHT'
                if event.key == pygame.K_DOWN:
                    change_to = 'DOWN'

            if change_to == 'UP' and direction != 'DOWN':
                direction = 'UP'
            if change_to == 'DOWN' and direction != 'UP':
                direction = 'DOWN'
            if change_to == 'LEFT' and direction != 'RIGHT':
                direction = 'LEFT'
            if change_to == 'RIGHT' and direction != 'LEFT':
                direction = 'RIGHT'    
        

#[---------------------------------]
#   movement and refresh sprite
#[---------------------------------]

        def movement():
            if direction == 'UP':
                position[1] -= 10
            if direction == 'DOWN':
                position[1] += 10
            if direction == 'LEFT':
                position[0] -= 10
            if direction == 'RIGHT':
                position[0] += 10


def game_over():        # End the game when condition is trigger
    global last_score

    # Game over text layout
    last_score = score
    game_over_text = pygame.font.Font(None, 50)
    game_over_frame = game_over_text.render('GAME OVER' + '  ' + f'Your score: {score}', True, white)
    game_over_set = game_over_frame.get_rect()
    game_over_set.midtop = (x / 2, y / 4)

    # Display the text
    window.blit(game_over_frame, game_over_set)

    # Refresh the screen
    pygame.display.flip()

    # Wait 2 sec before quiting the program
    time.sleep(2)
    game_menu()


def game_menu():        # Menu displaying last score and reset the game
    global Running
    global direction
    global change_to
    global body
    global position
    global last_score
    global score

    # Reset game
    Running = False
    body = [[100, 50], [90, 50], [80, 50], [70, 50]]
    position = [100, 50]
    direction = 'RIGHT'
    change_to = direction

    # Press space to play
    while not Running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    Running = True
                    mainloop()

        # Game_menu text layout
        game_menu_text = pygame.font.Font(None, 50)
        game_menu_frame = game_menu_text.render('PRESS SPACE TO START THE GAME', True, white)
        game_menu_set = game_menu_frame.get_rect()
        game_menu_set.midtop = (x / 2, y / 4)
        score_frame = game_menu_text.render(f'Last score : {last_score}', True, white)
        score_set = score_frame.get_rect()
        score_set.midbottom = (x / 2, y / 4)


        # Display the text
        window.blit(game_menu_frame, game_menu_set)
        window.blit(score_frame, score_set)

        # Refresh the screen
        pygame.display.flip()
        window.fill(black)

        score = 0


game_menu()