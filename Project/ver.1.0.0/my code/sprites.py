import pygame as pg
from settings import *
from random import choice
import random as rd
vec = pg.math.Vector2

class Player(pg.sprite.Sprite):
    def __init__(self, game):
        pg.sprite.Sprite.__init__(self)
        self.game = game

        self.load_images()

        self.pos = vec(40, HEIGHT - 100)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

        self.JUMP_HEIGHT = JUMP_HEIGHT

    def load_images(self):
        
        self.img = []
        for i in range(1, 4):

            ball_img = pg.image.load(f"assets/ball_{i}.png")
            ball_img = pg.transform.scale(ball_img, (WIDTH, HEIGHT))
            ball_img.set_colorkey((255, 255, 255))

            self.img.append(ball_img)

        self.image = self.img[0]
        self.rect = self.image.get_rect(x = START_X, bottom = START_Y)

    def jump(self):
        # jump only if standing on a platform
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

    def keyboard(self, event):

        to_x = 0

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RIGHT:
                to_x = VEL
            elif event.key == pg.K_LEFT:
                to_x = -1 * VEL

        self.rect.centerx += to_x


class Platform(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        pg.sprite.Sprite.__init__(self)

        self.plat = self.plat = pg.image.load("./assets/sample_platform.png")

        images = [0] * 10

        for i in range(10):

            width = rd.randrange(P_WIDTH_1, P_WIDTH_2)
            plat_img = pg.transform.scale(self.plat, (width, P_HEIGHT))

            images[i] = plat_img

        self.image = choice(images)
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

