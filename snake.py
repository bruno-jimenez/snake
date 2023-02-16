from tkinter import *
import pygame
import random
from pygame import event
import time
from sys import exit

#[---------------------------------]
# creating the window and setup 
#[---------------------------------]

pygame.init()
pygame.font.init()
speed = 10
fps = pygame.time.Clock()

# window setup
x=720
y=480
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

# Return a random number for spawn a apple into the screen
x=720
y=480
apple_spawn = False
apple = [random.randrange(1, (x//10))*10, random.randrange(1, (y//10))*10]


def game_over():        # End the game when condition is trigger
    global last_score

    # Game over text layout
    last_score = score
    game_over_text = pygame.font.Font(None, 50)
    game_over_frame = game_over_text.render('GAME OVER' + '  ' + f'Your score : {score}', True, white)
    game_over_set = game_over_frame.get_rect()
    game_over_set.midtop = (x / 2, y / 4)

    # Display the text
    window.blit(game_over_frame, game_over_set)

    # Refresh the screen
    pygame.display.flip()

    # Wait 2 sec before quiting the program
    time.sleep(2)
    game_menu()


# Create the physical form of the snake and apples
for pos in body:
    pygame.draw.rect(window, green, pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(window, red, pygame.Rect(apple[0], apple[1], 10, 10))

#[---------------------------------]
#    creating the loop
#[---------------------------------]

def main_loop():    # Main game loop
    global change_to
    global direction
    global apple
    global apple_spawn
    global score

    # Main loop
    while Running:
        for event in pygame.event.get():

            # Quit the program if close button is clicked
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

#[---------------------------------]
#         bind arrow key
#[---------------------------------]

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

        if direction == 'UP':
            position[1] -= 10
        if direction == 'DOWN':
            position[1] += 10
        if direction == 'LEFT':
            position[0] -= 10
        if direction == 'RIGHT':
            position[0] += 10

        body.insert(0, list(position))


#[---------------------------------]
#    feeding snake and grow it
#[---------------------------------]

        if position[0] == apple[0] and position[1] == apple[1]:
            apple_spawn = False
            score += score_increment
        else:
            body.pop()

#[---------------------------------]
#      spawn & respawn apple
#[---------------------------------]

        if not apple_spawn:
            apple = [random.randrange(1, (x // 10)) * 10, random.randrange(1, (y // 10)) * 10]
            apple_spawn = True

#[---------------------------------]
#   remove back of snake when move
#[---------------------------------]

        window.fill(black)

#[---------------------------------]
#  create shape for snake and apple
#[---------------------------------]

        for pos in body:
            pygame.draw.rect(window, green, pygame.Rect(pos[0], pos[1], 10, 10))
            pygame.draw.rect(window, red, pygame.Rect(apple[0], apple[1], 10, 10))


#[------------------------------------------]
#   condition of losing (wall & self touch )
#[------------------------------------------]

        if position[0] < 0 or position[0] > x - 10:
            game_over()
        if position[1] < 0 or position[1] > y - 10:
            game_over()


        for self in body[1:]:
            if position[0] == self[0] and position[1] == self[1]:
                game_over()

#[---------------------------------]
#      write score
#[---------------------------------]

        score_text = font.render(f'Score: {score}', True, (255, 255, 255))
        window.blit(score_text, (50, 50))

#[---------------------------------]
#      set the game refresh
#[---------------------------------]
        pygame.display.flip()
        fps.tick(speed)


def game_menu():       
    global Running
    global direction
    global change_to
    global body
    global position
    global last_score
    global score

  
    Running = False
    body = [[100, 50], [90, 50], [80, 50], [70, 50]]
    position = [100, 50]
    direction = 'RIGHT'
    change_to = direction


    while not Running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    Running = True
                    main_loop()

        
        game_menu_text = pygame.font.Font(None, 50)
        game_menu_frame = game_menu_text.render('PRESS SPACE TO START THE GAME', True, white)
        game_menu_set = game_menu_frame.get_rect()
        game_menu_set.midtop = (x / 2, y / 4)
        score_frame = game_menu_text.render(f'Last score : {last_score}', True, white)
        score_set = score_frame.get_rect()
        score_set.midbottom = (x / 2, y / 4)


        window.blit(game_menu_frame, game_menu_set)
        window.blit(score_frame, score_set)


        pygame.display.flip()
        window.fill(black)

        score = 0


game_menu()