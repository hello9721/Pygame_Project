import pygame as pg

def keyboard(event, to_x, speed):

    if event.type == pg.KEYDOWN:   # 키보드 입력값을 아스키코드로 변환
        if event.key == pg.K_RIGHT:
            to_x = speed
        elif event.key == pg.K_LEFT:
            to_x = -1 * speed

    return to_x