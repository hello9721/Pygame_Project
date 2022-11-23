import pygame as pg

# 색상표
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
YELLOW = (255, 255, 0)

# 객체의 위치 기준 좌표

# left centerx right width

# top
# centery
# bottom
# height

pg.init()
scr = pg.display.set_mode((800,800))
clk = pg.time.Clock()

smp_img = pg.image.load("./ball.png")
smp_img = pg.transform.scale(smp_img, (80, 80))
smp = smp_img.get_rect()                # 이미지를 게임 객체로 저장
smp.centerx = 400                       # x 좌표
smp.bottom = 800                        # y 좌표


while 1:                                # 메인 루프

    scr.fill(BLACK)

    event = pg.event.poll()
    if event.type == pg.QUIT: break

    scr.blit(smp_img, smp)              # 해당 위치에 이미지 그리기

    pg.display.update()
    clk.tick(30)

pg.quit()                               # 종료