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

large_font = pg.font.SysFont('malgungothic', 72)    # 게임 오버 폰트 로드
small_font = pg.font.SysFont('malgungothic', 36)    # 점수 폰트 로드
score = 0                                           # 점수 값 저장

game_over = False                                   # 게임 오버 조건 달성 여부 저장

smp_img = pg.image.load("./ball.png")
smp_img = pg.transform.scale(smp_img, (80, 80))
smp = smp_img.get_rect(centerx = 400, bottom = 800)


enm_img = pg.image.load("./bomb.png")
enm_img = pg.transform.rotate(enm_img, 45.0)

enms = []

for i in range(3):

    enm = enm_img.get_rect(top = -100)
    enm.left = random.randint(0, 800 - enm.width)
    enms.append(enm)


while 1:                                # 메인 루프

    scr.fill(BLACK)

    if not game_over:

        for event in pg.event.get():        # 전체 이벤트 반환
        
            if event.type == pg.QUIT: break
            elif event.type == pg.KEYDOWN:

                if event.key == pg.K_LEFT: smp.left -= 5
                elif event.key == pg.K_RIGHT: smp.left += 5

        for enm in enms:
            
            enm.top += 5

            if enm.top > 800:               # 위치 변화 보다 객체를 새로 만드는 형식으로 폭탄 리젠
                
                enms.remove(enm)
                enm = enm_img.get_rect(left = random.randint(0, 800 - enm.width), top = -100)
                enms.append(enm)
                score += 10                                 # 점수 값 증가

        for enm in enms:
            
            if enm.colliderect(smp): game_over = True       # 두 객체가 겹치면 게임오버 true

    score_img = small_font.render('점수 {}'.format(score), True, (255 ,255, 0))
                                                        # 점수 이미지로
    if game_over:
                                                        # 게임오버 글씨를 이미지로 바꾼뒤 임시 게임 객체로 표시
        go_img = large_font.render("GAME OVER", True, (255, 0, 0))
        scr.blit(go_img, go_img.get_rect(centerx = 400, centery = 400))

    if smp.left < 0: smp.left = 0
    elif smp.right > 800: smp.right = 800

    for enm in enms: scr.blit(enm_img, enm)
    scr.blit(smp_img, smp)
    scr.blit(score_img, (10, 10))                       # 점수 이미지 표시

    pg.display.update()
    clk.tick(30) 

pg.quit()                               # 종료