import pygame as pg
import lib

pg.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 500

scr = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clk = pg.time.Clock() 
pg.key.set_repeat(100, 10)

ball_img = pg.image.load("./assets/sample_ball.png")
ball_img = pg.transform.scale(ball_img, (50, 50))
ball = ball_img.get_rect(bottom = SCREEN_HEIGHT, centerx = SCREEN_WIDTH/2)

to_x = 0

while True:

    scr.fill((0, 0, 0))

    for event in pg.event.get():
        if event.type == pg.QUIT:
            break
        x = lib.keyboard(event, to_x, 3)

        ball.centerx += x
    
    y = SCREEN_HEIGHT - ball.bottom
    
    if 0 <= y <= 100: y += 0.1
    elif y >= 100: y -= 0.1
    elif y < 0: y = 0

    ball.bottom = y

    scr.blit(ball_img, ball)

    pg.display.update()
    clk.tick(30)

pg.quit() 
