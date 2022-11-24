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

large_font = pg.font.SysFont('malgungothic', 72)
small_font = pg.font.SysFont('malgungothic', 36)
score = 0

game_over = False

smp_img = pg.image.load("ball2.png")
smp_img = pg.transform.scale(smp_img, (80, 80))
smp = smp_img.get_rect(centerx = 400, bottom = 800)


enm_img = pg.image.load("bomb.png")
enm_img = pg.transform.rotate(enm_img, 45.0)

enms = []

for i in range(5):

    enm = enm_img.get_rect(top = -100)
    enm.left = random.randint(0, 800 - enm.width)
    dy = random.randint(5, 15)           # 속도 랜덤 조절
    enms.append((enm, dy))


while 1:                                # 메인 루프

    scr.fill(BLACK)

    if not game_over:

        for event in pg.event.get():        # 전체 이벤트 반환
        
            if event.type == pg.QUIT: break
            elif event.type == pg.KEYDOWN:

                if event.key == pg.K_LEFT: smp.left -= 5
                elif event.key == pg.K_RIGHT: smp.left += 5

        for enm, dy in enms:
            
            enm.top += dy                   # 움직이는 범위를 조절하여 속도 조절

            if enm.top > 800:
                
                enms.remove((enm, dy))
                enm = enm_img.get_rect(left = random.randint(0, 800 - enm.width), top = -100)
                dy = random.randint(5, 15)
                enms.append((enm, dy))
                score += 10

        for enm, dy in enms:
            
            if enm.colliderect(smp): game_over = True

    score_img = small_font.render('점수 {}'.format(score), True, (255 ,255, 0))
    
    if game_over:
        
        go_img = large_font.render("GAME OVER", True, (255, 0, 0))
        scr.blit(go_img, go_img.get_rect(centerx = 400, centery = 400))

    if smp.left < 0: smp.left = 0
    elif smp.right > 800: smp.right = 800

    for enm, dy in enms: scr.blit(enm_img, enm)
    scr.blit(smp_img, smp)
    scr.blit(score_img, (10, 10))

    pg.display.update()
    clk.tick(30) 

pg.quit()                               # 종료
