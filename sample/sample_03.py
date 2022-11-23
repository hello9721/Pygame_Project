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
pg.key.set_repeat(100, 10)              # (time, step) ms
                                        # 첫 이벤트 후 time 이후에도 지속이 된다면
                                        # 두번째 이벤트로 간주
                                        # 그 이후 step 마다 지속 시 이벤트로 간주


smp_img = pg.image.load("./ball.png")
smp_img = pg.transform.scale(smp_img, (80, 80))
smp = smp_img.get_rect(centerx = 400, bottom = 800)
                                        # 이미지를 게임 객체로 저장


while 1:                                # 메인 루프

    scr.fill(BLACK)

    for event in pg.event.get():        # 전체 이벤트 반환
        
        if event.type == pg.QUIT: break # 루프 중지 조건문
        elif event.type == pg.KEYDOWN:
                                        # 방향키 누르는 이벤트 발생시 객체 이동
            if event.key == pg.K_LEFT: smp.left -= 5
            elif event.key == pg.K_RIGHT: smp.left += 5

    if smp.left < 0: smp.left = 0
    elif smp.right > 800: smp.right = 800
                                        # 화면 너머로 가지 못하도록 벽처리

    scr.blit(smp_img, smp)

    pg.display.update()
    clk.tick(30) 

pg.quit()                               # 종료