import pygame as pg
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
        self.rect = self.ball_img.get_rect(centerx = SCRWIDTH/2, bottom = SCRHEIGHT)

    def keyboard(self, event):

        to_x = 0

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RIGHT:
                to_x = VEL
            elif event.key == pg.K_LEFT:
                to_x = -1 * VEL

        self.rect.centerx += to_x

    def jump(self):

        if self.JUMP_HEIGHT == 11:

            self.ball_img = self.img[2]
            self.JUMP_HEIGHT -= 1

        elif self.JUMP_HEIGHT > -11:

            self.ball_img = self.img[1]

            n = 1
            if self.JUMP_HEIGHT < 0: n = -1

            self.rect.bottom -= (self.JUMP_HEIGHT ** 2) * n * 0.5
            self.JUMP_HEIGHT -= 1

        elif self.JUMP_HEIGHT == -11:

            self.ball_img = self.img[2]
            self.JUMP_HEIGHT -= 1

        else:

            self.JUMP_HEIGHT = 11
            self.rect.bottom = SCRHEIGHT