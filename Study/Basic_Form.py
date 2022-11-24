import pygame as pg

pg.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800

scr = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clk = pg.time.Clock() 

bg_img = pg.image.load('background.png')

while True:

    scr.blit(bg_img, (0, 0))

    for event in pg.event.get():
        if event.type == pg.QUIT:
            break

    pg.display.update()
    clk.tick(30)

pg.quit() 
