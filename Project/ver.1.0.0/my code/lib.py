import pygame as pg
from SETTINGS import *

def keyboard(event, to_x, speed):

    if event.type == pg.KEYDOWN:   # 키보드 입력값을 아스키코드로 변환
        if event.key == pg.K_RIGHT:
            to_x = speed
        elif event.key == pg.K_LEFT:
            to_x = -1 * speed

    return to_x

def jump(img, ball):

    if JUMP_HEIGHT == 11:
        ball_img = img[2]
        JUMP_HEIGHT -= 1
    elif JUMP_HEIGHT > -11:
        ball_img = img[1]
        n = 1
        if JUMP_HEIGHT < 0: n = -1
        ball.bottom -= (JUMP_HEIGHT ** 2) * n * 0.5
        JUMP_HEIGHT -= 1
    elif JUMP_HEIGHT == -11:
        ball_img = img[2]
        JUMP_HEIGHT -= 1
    else:
        JUMP_HEIGHT = 11
        ball.bottom = SCRHEIGHT

    return ball_img