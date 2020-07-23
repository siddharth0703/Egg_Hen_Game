from math import hypot
from random import randint

import pygame

pygame.init()
# Screen Size
screen = pygame.display.set_mode((1000, 700))
running = True
# Score
score_value = 0
font = pygame.font.SysFont('forte', 30)

text_x = 10
text_y = 10
# Icon and Title and Background
pygame.display.set_caption('Egg and Hen Game')
icon = pygame.image.load('1.png')
pygame.display.set_icon(icon)
background = pygame.image.load('soc.jpg')
# Player
playerimage = pygame.image.load('hen.png')
player_x_axis = 371
player_y_axis = 480
player_x_value_change = 0
# Enemy
enemyimage = pygame.image.load('shopping-basket.png')
e1_x_axis = randint(0, 800)
e1_y_axis = randint(120, 240)
enemy_x_value_change = 0.09
enemy_y_value_change = 0.0
# Egg
# Ready : you cant see bullet on screen ; Fire : Bullet is currently moving
eggimage = pygame.image.load('egg.png')
egg_x_axis = 0
egg_y_axis = 480
egg_x_value_change = 0.00
egg_y_value_change = 1
egg_state = 'ready'


# MY PLAYER DEFINED
def player(x, y):
    screen.blit(playerimage, (x, y))


# MY ENEMY DEFINED
def my_enemy(x, y):
    screen.blit(enemyimage, (x, y))


def fire_egg(x, y):
    global egg_state
    egg_state = 'fire'
    screen.blit(eggimage, (x + 16, y + 10))


def isCollision(egg_x, egg_y, bucket_x, bucket_y):
    distance = hypot(bucket_y - egg_y, bucket_x - egg_x)
    if distance < 27:
        return True
    return False


# Font Score
def scorecard(x, y):
    textsurface = font.render('Score : ' + str(score_value), True, (0, 0, 0))
    screen.blit(textsurface, (0, 0))


# GameLoop
while running:
    # rgb
    screen.fill((0, 255, 0))
    # screen.blit(background, (0, 0))
    for event in pygame.event.get():  # Gathers all events
        if event.type == pygame.QUIT:
            running = False
        # if  key is pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_value_change = -0.7
                print('LEFT ARROW KEY IS PRESSED')
            if event.key == pygame.K_RIGHT:
                player_x_value_change = 0.7
                print('Right ARROW KEY IS PRESSED')
            if event.key == pygame.K_SPACE:
                if egg_state == 'ready':
                    egg_x_axis = player_x_axis
                    fire_egg(egg_x_axis, egg_y_axis)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_value_change = 0.0
                print('RELEASED')
    # Playermovement
    player_x_axis += player_x_value_change

    if player_x_axis < 0:
        player_x_axis = 0
    elif player_x_axis >= 736:
        player_x_axis = 736
    # Enemy Movement
    e1_x_axis += enemy_x_value_change
    e1_y_axis += enemy_y_value_change

    if e1_x_axis < 0:
        enemy_x_value_change = 0.3
        e1_y_axis += enemy_y_value_change
    elif e1_x_axis >= 736:
        enemy_x_value_change = -0.03
        e1_y_axis += enemy_y_value_change

    # Egg(this state runs when SPACE KEY is pressed
    if egg_y_axis <= 0:
        egg_y_axis = 480
        egg_state = 'ready'
    if egg_state == 'fire':
        fire_egg(egg_x_axis, egg_y_axis)
        egg_y_axis -= egg_y_value_change
    # Collision
    collision = isCollision(egg_x_axis, egg_y_axis, e1_x_axis, e1_y_axis)
    if collision:
        egg_state = 'ready'
        egg_y_axis = 480
        score_value += 1
        print("Score ", score_value)
        e1_x_axis = randint(0, 735)
        e1_y_axis = randint(120, 240)

    player(player_x_axis, player_y_axis)
    scorecard(text_x, text_y)
    my_enemy(e1_x_axis, e1_y_axis)
    pygame.display.update()
