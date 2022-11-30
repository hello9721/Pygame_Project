import pygame as pg
from SPRITES import *
from SETTINGS import *

class Game:

    def __init__(self):
        
        pg.init()

        self.scr = pg.display.set_mode((SCRWIDTH,SCRHEIGHT))
        pg.display.set_caption(TITLE)

        self.run = True
        self.ball = Player()

    def running(self):

        for event in pg.event.get():

            if event.type == pg.QUIT: self.run = False

            self.ball.keyboard(event)

            if self.ball.rect.x < -5: self.ball.rect.x = -5
            elif self.ball.rect.x > SCRWIDTH - WIDTH + 5: self.ball.rect.x = SCRWIDTH - WIDTH + 5
    
        self.ball.jump()
        
        self.scr.fill((0,0,0))
        self.scr.blit(self.ball.ball_img, self.ball.rect)
        pg.display.update()


g = Game()

while g.run:
    pg.time.delay(FPS)
    g.running()

pg.quit()