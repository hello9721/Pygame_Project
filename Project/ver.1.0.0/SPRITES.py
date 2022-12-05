import pygame as pg
import random as rd
from SETTINGS import *

class Player:

    def __init__(self):
        
        pg.key.set_repeat(KEY_REPEAT_1, KEY_REPEAT_2)

        self.JUMP = False
        self.JUMP_HEIGHT = JUMP_HEIGHT
        self.x = 0

        self.get_img()

    def get_img(self):

        self.img = []
        for i in range(1, 4):

            ball_img = pg.image.load(f"assets/ball_{i}.png")
            ball_img = pg.transform.scale(ball_img, (WIDTH, HEIGHT))
            ball_img.set_colorkey((255, 255, 255))

            self.img.append(ball_img)

        self.ball_img = self.img[0]
        self.rect = self.ball_img.get_rect(x = START_X, bottom = START_Y)

    def keyboard(self, event):

        to_x = 0

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RIGHT:
                to_x = VEL
            elif event.key == pg.K_LEFT:
                to_x = -1 * VEL

        self.rect.centerx += to_x

    def jump(self):

        if self.JUMP_HEIGHT == JUMP_HEIGHT:

            self.ball_img = self.img[2]
            self.JUMP_HEIGHT -= 1

        elif self.JUMP_HEIGHT > -JUMP_HEIGHT:

            self.ball_img = self.img[1]

            n = 1
            if self.JUMP_HEIGHT < 0: n = -1

            self.rect.bottom -= (self.JUMP_HEIGHT ** 2) * n * 0.5
            self.JUMP_HEIGHT -= 1

        elif self.JUMP_HEIGHT == -JUMP_HEIGHT:

            self.ball_img = self.img[2]
            self.JUMP_HEIGHT -= 1

        else:

            self.JUMP_HEIGHT = JUMP_HEIGHT
            self.rect.bottom = SCRHEIGHT


class Platform:

    def __init__(self, game):

        width = 100 
        self.x = 0
        self.y = START_Y
        self.game = game

        self.plat = pg.image.load("./assets/sample_platform.png")
        self.plat_img = pg.transform.scale(self.plat, (width, P_HEIGHT))
        self.rect = self.plat_img.get_rect(left = self.x, top = self.y + 10)

    def random_platform(self):

        random_width = rd.randrange(P_WIDTH_1, P_WIDTH_2)
        self.x = rd.randrange(0, SCRWIDTH - random_width + 20, 11)
        self.y = SCRHEIGHT + rd.randrange(-600, -120, 60)

        collide = True

        while collide:

            if len(self.game.p_rect) != 0:
        
                for i in self.game.p_rect:
                    
                    if self.rect.colliderect(i):

                        if i.left >= SCRWIDTH/2: x_range = (0, SCRWIDTH/2)
                        elif i.left < SCRWIDTH/2: x_range = (SCRWIDTH/2, SCRWIDTH)

                        if i.centery >= SCRHEIGHT/2: y_range = (SCRHEIGHT/2, SCRHEIGHT)
                        elif SCRHEIGHT/2 > i.centery: y_range = (0, SCRHEIGHT/2)

                        self.x = rd.randrange(x_range[0], x_range[1])
                        self.y = rd.randrange(y_range[0], y_range[1])

                    else: collide = False            
            
        self.plat_img = pg.transform.scale(self.plat, (random_width, P_HEIGHT))
        self.rect = self.plat_img.get_rect(left = self.x, top = self.y)
