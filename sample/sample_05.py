import pygame as pg
import random

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
pg.key.set_repeat(100, 10)

smp_img = pg.image.load("./ball.png")
smp_img = pg.transform.scale(smp_img, (80, 80))
smp = smp_img.get_rect(centerx = 400, bottom = 800)


enm_img = pg.image.load("./bomb.png")
enm_img = pg.transform.rotate(enm_img, 45.0)

enms = []                                       # 폭탄이 여러개 떨어져야 하므로
                                                # 여러 위치의 폭탄 객체를 리스트로 만든다.

for i in range(3):

    enm = enm_img.get_rect(left = random.randint(0, 800), top = -100)
    enms.append(enm)                            # x 좌표는 무작위, 안보이도록 -100 위치에서 생성


while 1:                                # 메인 루프

    scr.fill(BLACK)

    for event in pg.event.get():        # 전체 이벤트 반환
        
        if event.type == pg.QUIT: break
        elif event.type == pg.KEYDOWN:

            if event.key == pg.K_LEFT: smp.left -= 5
            elif event.key == pg.K_RIGHT: smp.left += 5

    for enm in enms: enm.top += 5                   # while이 진행됨에 따라 폭탄의 위치가 점점 아래로 내려온다.

    if smp.left < 0: smp.left = 0
    elif smp.right > 800: smp.right = 800

    for enm in enms: scr.blit(enm_img, enm)         # 폭탄 객체 여러개 화면에 생성
    scr.blit(smp_img, smp)

    pg.display.update()
    clk.tick(30) 

pg.quit()                               # 종료