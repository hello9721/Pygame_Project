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
        self.platform = Platform(self)
        self.p_rect = [self.platform.rect]
        self.p_img = [self.platform.plat_img]

        self.running()

    def running(self):

        while self.run:

            pg.time.delay(FPS)

            self.key_events()
            self.update()
        

    def update(self):

        for i in range(NUM_PLAT - len(self.p_rect)):
            
            self.platform.random_platform()

            self.p_rect.append(self.platform.rect)
            self.p_img.append(self.platform.plat_img)

        for i in range(len(self.p_rect)): self.scr.blit(self.p_img[i], self.p_rect[i])

        pg.display.update()

    def key_events(self):

        for event in pg.event.get():

            if event.type == pg.QUIT: self.run = False

            self.ball.keyboard(event)

            if self.ball.rect.x < -5: self.ball.rect.x = -5
            elif self.ball.rect.x > SCRWIDTH - WIDTH + 5: self.ball.rect.x = SCRWIDTH - WIDTH + 5
    
        self.ball.jump()
        
        self.scr.fill((0,0,0))
        self.scr.blit(self.ball.ball_img, self.ball.rect)


g = Game()

pg.quit()