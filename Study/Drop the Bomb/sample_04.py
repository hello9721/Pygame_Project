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
pg.key.set_repeat(100, 10)

smp_img = pg.image.load("./ball.png")
smp_img = pg.transform.scale(smp_img, (80, 80))
smp = smp_img.get_rect(centerx = 400, bottom = 800)


enm_img = pg.image.load("./bomb.png")               # 적 이미지 로드
enm_img = pg.transform.rotate(enm_img, 45.0)        # 각도 조정
enm = enm_img.get_rect(centerx = 400, centery = 400)# 위치 조정


while 1:                                # 메인 루프

    scr.fill(BLACK)

    for event in pg.event.get():        # 전체 이벤트 반환
        
        if event.type == pg.QUIT: break
        elif event.type == pg.KEYDOWN:

            if event.key == pg.K_LEFT: smp.left -= 5
            elif event.key == pg.K_RIGHT: smp.left += 5


    if smp.left < 0: smp.left = 0
    elif smp.right > 800: smp.right = 800

    scr.blit(smp_img, smp)
    scr.blit(enm_img, enm)              # 스크린에 이미지 띄우기

    pg.display.update()
    clk.tick(30) 

pg.quit()                               # 종료