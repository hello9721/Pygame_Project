import pygame as pg
from settings import *
from random import choice
vec = pg.math.Vector2


class Spritesheet:
    # Utility class for loading spritesheets
    def __init__(self, filename):
        self.spritesheet = pg.image.load(filename).convert()

    def get_image(self, x, y, width, height):
        # Grab an image out of a lager spritesheet
        image = pg.Surface((width, height))
        image.blit(self.spritesheet, (0, 0), (x, y, width, height)) # blit = 이미지 복사 / blit(복사할 이미지, 복사할 대상)
        image = pg.transform.scale(image, (width//2, height//2))
        return image


class Player(pg.sprite.Sprite):
    def __init__(self, game):
        pg.sprite.Sprite.__init__(self)
        self.game = game

        self.walking = False
        self.jumping = False
        self.current_frame = 0
        self.last_update = 0

        self.load_images()
        self.image = self.standing_frames[0]

        self.rect = self.image.get_rect()
        self.rect.center = (40, HEIGHT - 100)

        self.pos = vec(40, HEIGHT - 100)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

    def load_images(self):
        self.standing_frames = [self.game.spritesheet.get_image(614, 1063, 120, 191),
                                self.game.spritesheet.get_image(690, 406, 120, 201)]
        for frame in self.standing_frames:
            frame.set_colorkey(BLACK)

        self.walk_frames_r = [self.game.spritesheet.get_image(678, 860, 120, 201),
                              self.game.spritesheet.get_image(692, 1458, 120, 207)]
        for frame in self.walk_frames_r:
            frame.set_colorkey(BLACK)

        self.walk_frames_l = [pg.transform.flip(frame, True, False)
                              for frame in self.walk_frames_r]

        self.jump_frame = self.game.spritesheet.get_image(382, 763, 150, 181)
        self.jump_frame.set_colorkey(BLACK)

    def jump_cut(self):
        if self.jumping:
            if self.vel.y < -3:
                self.vel.y = -3

    def jump(self):
        # jump only if standing on a platform
        self.rect.y += 0.1
        hits = pg.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.y -= 0.1
        if hits and not self.jumping:
            self.jumping = True
            self.vel.y = -PLAYER_JUMP

    def update(self):
        self.animate()
        self.acc = vec(0, PLAYER_GRAVITY)
        keys = pg.key.get_pressed()

        if keys[pg.K_LEFT]:
            self.acc.x = -PLAYER_ACC
        if keys[pg.K_RIGHT]:
            self.acc.x = PLAYER_ACC

        self.acc.x += self.vel.x*PLAYER_FRICTION
        self.vel += self.acc
        if abs(self.vel.x) < 0.1:
            self.vel.x = 0
        self.pos += self.vel + 0.5*self.acc

        if self.pos.x > WIDTH + self.rect.width/2:
            self.pos.x = 0 - self.rect.width/2
        if self.pos.x < 0 - self.rect.width/2:
            self.pos.x = WIDTH + self.rect.width/2

        self.rect.midbottom = self.pos

    def animate(self):
        now = pg.time.get_ticks()

        if self.vel.x != 0:
            self.walking = True
        else:
            self.walking = False

        if self.walking:
            if now - self.last_update > 200:
                self.last_update = now
                self.current_frame = ((self.current_frame + 1)
                                      % len(self.walk_frames_l))

                bottom = self.rect.bottom
                if self.vel.x > 0:
                    self.image = self.walk_frames_r[self.current_frame]
                else:
                    self.image = self.walk_frames_l[self.current_frame]
                    self.rect = self.image.get_rect()
                    self.rect.bottom = bottom

        if not self.jumping and not self.walking:
            if (now - self.last_update) > 350:
                self.last_update = now
                self.current_frame = ((self.current_frame + 1)
                                      % len(self.standing_frames))
                bottom = self.rect.bottom
                self.image = self.standing_frames[self.current_frame]
                self.rect = self.image.get_rect()
                self.rect.bottom = bottom


class Platform(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        pg.sprite.Sprite.__init__(self)
        self.game = game

        images = [self.game.spritesheet.get_image(0, 288, 380, 94),
                  self.game.spritesheet.get_image(213, 1662, 201, 100)]

        self.image = choice(images)
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

