import pygame as pg
import random
from settings import *
from sprites import *
from os import path


class Game:
    def __init__(self):
        # initialize game window, etc
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True
        self.font_name = pg.font.match_font(FONT_NAME)
        self.load_data()

    def load_data(self):
        # Load high score
        self.dir = path.dirname(__file__) # 파일이 위치한 경로
        img_dir = path.join(self.dir, 'img') # 이미지 파일 경로
        try:
            with open(path.join(self.dir, HS_FILE), 'r') as f:
                self.highscore = int(f.read())
        except FileNotFoundError:
            self.highscore = 0

        # load spritesheet image
        self.spritesheet = Spritesheet(path.join(img_dir, SPRITESHEET))

    def new(self):
        # start a new game
        self.score = 0
        self.all_sprites = pg.sprite.Group() # 스프라이트 그룹 생성
        self.platforms = pg.sprite.Group()

        self.player = Player(self) # Player 객체 생성
        self.all_sprites.add(self.player) # 스프라이트 그룹에 객체 추가

        for plat in PLATFORM_LIST:
            p = Platform(self, *plat)
            self.all_sprites.add(p)
            self.platforms.add(p)

        self.run()

    def run(self):
        # Game Loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        # Game Loop - Update
        self.all_sprites.update()
        # check if player hits a platfrom
        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player, self.platforms, False)
            if hits:
                lowest = hits[0]
                for hit in hits:
                    if hit.rect.bottom > lowest.rect.bottom:
                        lowest = hit
                if self.player.pos.y < lowest.rect.centery:
                    self.player.pos.y = lowest.rect.top + 0.1
                    self.player.vel.y = 0
                    self.player.jumping = False

        # If player reached top 1/4 of screen
        if self.player.rect.top <= HEIGHT/4:
            self.player.pos.y += max(abs(self.player.vel.y), 5)
            for plat in self.platforms:
                plat.rect.y += max(abs(self.player.vel.y), 5)
                if plat.rect.top >= HEIGHT:
                    plat.kill()
                    self.score += 10

        # Die
        if self.player.rect.bottom > HEIGHT:
            for sprite in self.all_sprites:
                sprite.rect.y -= max(self.player.vel.y, 10)
                if sprite.rect.bottom < 0:
                    sprite.kill()
        if len(self.platforms) == 0:
            self.playing = False

        # Spawn new platforms
        while len(self.platforms) < 6:
            width = random.randrange(50, 100)
            p = Platform(self, random.randrange(0, WIDTH - width),
                         random.randrange(-75, -30))
            self.platforms.add(p)
            self.all_sprites.add(p)

    def events(self):
        # Game Loop - Events
        for event in pg.event.get():
            # check for closing window
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
                
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.player.jump()
            if event.type == pg.KEYUP:
                if event.key == pg.K_SPACE:
                    self.player.jump_cut()

    def draw(self):
        # Game Loop - Draw
        self.screen.fill(BGCOLOR)
        self.all_sprites.draw(self.screen)
        self.screen.blit(self.player.image, self.player.rect)
        self.draw_text(str(self.score), 22, WHITE, WIDTH/2, 15)

        # *after* drawing everything, flip the display
        pg.display.flip()

    def show_start_screen(self):
        # game splash/start screen
        self.screen.fill(BGCOLOR)
        self.draw_text(TITLE, 48, WHITE, WIDTH/2, HEIGHT/4)
        self.draw_text("Arrows to move, Space to jump",
                       22, WHITE, WIDTH/2, HEIGHT/2)
        self.draw_text("Press a key to play",
                       22, WHITE, WIDTH/2, HEIGHT*3/4)
        self.draw_text("High Score : " + str(self.highscore),
                       22, WHITE, WIDTH/2, 15)
        pg.display.flip()
        self.wait_for_key()

    def show_go_screen(self):
        # game over/continue
        if not self.running:
            return
        self.screen.fill(BGCOLOR)
        self.draw_text("GAME OVER", 48, WHITE, WIDTH/2, HEIGHT/4)
        self.draw_text("Score : " + str(self.score),
                       22, WHITE, WIDTH/2, HEIGHT/2)
        self.draw_text("Press a key to play again",
                       22, WHITE, WIDTH/2, HEIGHT*3/4)
        if self.score > self.highscore:
            self.highscore = self.score
            self.draw_text("NEW HIGH SCORE!",
                           22, WHITE, WIDTH/2, HEIGHT/2 + 40)
            with open(path.join(self.dir, HS_FILE), 'w') as f:
                f.write(str(self.score))
        else:
            self.draw_text("High Score : " + str(self.highscore),
                           22, WHITE, WIDTH/2, 15)

        pg.display.flip()
        self.wait_for_key()

    def wait_for_key(self):
        waiting = True
        while waiting:
            self.clock.tick(FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    waiting = False
                    self.running = False
                if event.type == pg.KEYUP:
                    waiting = False

    def draw_text(self, text, size, color, x, y):
        font = pg.font.Font(self.font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)


g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.show_go_screen()

pg.quit()