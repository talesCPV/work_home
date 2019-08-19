#!/usr/bin/python3

import pygame
import random
from pygame.locals import *

move = [50,100]
clock = pygame.time.Clock()
fps = 8
sentido = 3
hitbox = 8
screen_size = 520
rock = [0,0]
tail = []
in_play = True
restart = False


pygame.init()
screen = pygame.display.set_mode((screen_size,screen_size), 0, 32)
pygame.display.set_caption('Snake')

def print_text(surface, position, text, size, colour):
    font = pygame.font.get_default_font()
    font_layer = pygame.font.Font(font, size)
    font_surface = font_layer.render(text, True, colour)
    surface.blit(font_surface, position)
    return

def change_rock(t):
    global fps
    rock[0] = random.randint(0,510)
    rock[1] = random.randint(0,510)
    if t:
        tail.append([0,0])
        fps += 1

def set_tail():
    if len(tail) > 0:

        i=0
        while i < len(tail)-1:
            tail[i][0] = tail[i+1][0]
            tail[i][1] = tail[i+1][1]

            i += 1
        tail[-1][0] = move [0]
        tail[-1][1] = move [1]

        for i in range(len(tail)):
            pygame.draw.rect(screen, (255, 255, 255), [tail[i][0], tail[i][1]] + [10, 10], 0)


def run():

    set_tail()

    if sentido == 1:
        move[1] -= 10
    elif sentido == 2:
        move[1] += 10
    elif sentido == 3:
        move[0] += 10
    elif sentido == 4:
        move[0] -= 10


def game_over():
    if move in tail:
        return True
    else:
        if (move[0] > 1 and move[0] < screen_size-10) and (move[1] > 1 and move[1] < screen_size-10):
            return False
        else:
            return True

change_rock(0)

while True:
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == KEYDOWN:
            if event.key == 273: #up
                sentido = 1

            if event.key == 274:  # down
                sentido = 2

            if event.key == 275:  # right
                sentido = 3

            if event.key == 276:  # left
                sentido = 4

            if event.key == 32:  # space
                restart = True

    screen.fill([0, 0, 0])
    if game_over():
        print_text(screen, (screen_size//2 - 80,screen_size//2- 20), 'GAME OVER', 25, (0, 255, 0))
        print_text(screen, (screen_size//2 - 80,screen_size- 15), 'Press space to restart ', 15, (255, 255, 255))
        in_play = False

    else:
        run()

    if not in_play:
        if restart:
            move = [50, 100]
            fps = 8
            sentido = 3
            rock = [0, 0]
            tail = []
            in_play = True
            restart = False
            change_rock(0)

    print_text(screen, (screen_size-120, 10), 'score:'+str(len(tail)), 25, (0, 255, 0))
    pygame.draw.rect(screen, (255,255,255), [move[0], move[1]] + [10, 10], 0)
    pygame.draw.rect(screen, (255,0,0), [rock[0], rock[1]] + [10, 10], 0)
    pygame.display.update()

    if (move[0] >= rock[0]-hitbox and move[0] <= rock[0]+hitbox) and (move[1] >= rock[1]-hitbox and move[1] <= rock[1]+hitbox):
        change_rock(1)
