import pygame as pg
from lib import *
from SETTINGS import *

pg.init()

scr = pg.display.set_mode((SCRWIDTH,SCRHEIGHT))
pg.display.set_caption(TITLE)
pg.key.set_repeat(KEY_REPEAT_1, KEY_REPEAT_2)

img = []
for i in range(1, 4):

    ball_img = pg.image.load(f"assets/ball_{i}.png")
    ball_img = pg.transform.scale(ball_img, (WIDTH, HEIGHT))
    ball_img.set_colorkey((255, 255, 255))

    img.append(ball_img)

ball = img[0].get_rect(centerx = SCRWIDTH/2, bottom = SCRHEIGHT)

run = True

JUMP = False
x = 0

while run:
    pg.time.delay(30)                                               # 애니메이션 속도조절

    for event in pg.event.get():                                    # 키보드 입력 받기

        if event.type == pg.QUIT: run = False
        pos = keyboard(event, x, VEL)

        ball.centerx += pos
        if ball.x < -5: ball.x = -5
        elif ball.x > SCRWIDTH - WIDTH + 5: ball.x = SCRWIDTH - WIDTH + 5
    
    ball_img = jump(img, ball)
    
    scr.fill((0,0,0))
    scr.blit(ball_img, ball)
    pg.display.update() 
    
pg.quit()