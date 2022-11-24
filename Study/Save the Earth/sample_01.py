import pygame as pg
import random as rd

pg.init()

scr_width = 600
scr_height = 900

YELLOW = (255, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

small_font = pg.font.SysFont('malgungothic', 36)
score = 0

scr = pg.display.set_mode((scr_width, scr_height))
clk = pg.time.Clock()
cnt = 0

bg_img = pg.image.load('bg.png')            # 배경 이미지 설정

health_img = pg.image.load('health.png')    # 남은 목숨 수
health_img = pg.transform.scale(health_img, (36, 36))
health_cnt = 5

gameover = False

crush_img = pg.image.load('crush.png')      # 충돌 이미지 설정
bang = []

plane_img = pg.image.load('plane.png')      # 비행기 이미지 설정 및 객체화
plane = plane_img.get_rect(centerx = scr_width/2, bottom = scr_height)

atk_img = pg.image.load('rocket.png')       # 미사일 이미지 설정
atk_img = pg.transform.rotate(atk_img, 45.0)
atks = []

small_meteo = pg.image.load('meteo1.png')   # 작은 운석 이미지 설정
small_meteo = pg.transform.rotate(small_meteo, 45.0)

big_meteo = pg.image.load('meteo2.png')     # 큰 운석 이미지 설정
big_meteo = pg.transform.rotate(big_meteo, 45.0)

meteo_size = [big_meteo, small_meteo]       # 리스트로
meteos = []
n_meteo = 3

for i in range(n_meteo):                          # 소환할 운석들 사이즈, 속도 랜덤으로 생성

    n = rd.randint(0, 1)
    meteo = meteo_size[n].get_rect(top = -100)
    meteo.left = rd.randint(0, scr_width - meteo_size[n].get_width())

    dy = rd.randint(5, 12)
    
    meteos.append(((meteo_size[n], meteo), dy))

while True:

    try:

        if not gameover:

            for event in pg.event.get():

                if event.type == pg.KEYDOWN:
                
                    if event.key == pg.K_ESCAPE: pg.quit()
                    elif event.key == pg.K_SPACE:   # 스페이스 바가 눌렸을 때

                        atk = atk_img.get_rect(centerx = plane.centerx, top = plane.top)
                        atks.append(atk)

            
            pressed = pg.key.get_pressed()          # 키 이벤트 연속 처리

            if pressed[pg.K_LEFT]: plane.left -= 15
            elif pressed[pg.K_RIGHT]: plane.right += 15
            elif pressed[pg.K_UP]: plane.top -= 15
            elif pressed[pg.K_DOWN]: plane.bottom += 15

            for meteo, dy in meteos:                # 운석 아래로 떨어지기

                meteo[1].top += dy
                
                if meteo[1].top > scr_height:       # 운석 계속 생성

                    meteos.remove((meteo, dy))

                    health_cnt -= 1

                    if health_cnt == 0 : gameover = True

                    n = rd.randint(0, 1)
                    meteo = meteo_size[n].get_rect(top = -100)
                    meteo.left = rd.randint(0, scr_width - meteo_size[n].get_width())

                    dy = rd.randint(5, 12)
                    
                    meteos.append(((meteo_size[n], meteo), dy))

            
            for atk in atks:                        # 미사일 날리기

                atk.top -= 9
                if atk.top < 0: atks.remove(atk)

            for m, dy in meteos:                # 충돌 처리

                for atk in atks:

                    if atk.colliderect(m[1]):

                        crush = crush_img.get_rect(centerx = atk.centerx, centery = atk.top)
                        bang.append(crush)

                        meteos.remove((m, dy))
                        atks.remove(atk)

                        score += 100

                        n = rd.randint(0, 1)
                        meteo = meteo_size[n].get_rect(top = -100)
                        meteo.left = rd.randint(0, scr_width - meteo_size[n].get_width())

                        dy = rd.randint(5, 12)
                        
                        meteos.append(((meteo_size[n], meteo), dy))

            for meteo, dy in meteos:                    # 비행기와 운석 충돌 처리

                if plane.colliderect(meteo[1]):
                
                    meteos.remove((meteo, dy))

                    n = rd.randint(0, 1)
                    meteo = meteo_size[n].get_rect(top = -100)
                    meteo.left = rd.randint(0, scr_width - meteo_size[n].get_width())

                    dy = rd.randint(5, 12)
                    
                    meteos.append(((meteo_size[n], meteo), dy))

                    health_cnt -= 1
                    if health_cnt == 0: gameover = True

            if score%5000 == 0: n_meteo += 2

            if plane.left < 0: plane.left = 0       # 비행기 스크린 밖으로 나가지 않도록 벽처리
            elif plane.right > 600: plane.right = 600
            elif plane.bottom > 900: plane.bottom = 900
            elif plane.top < 0: plane.top = 0

            scr.blit(bg_img, (0, 0))                # 스크린에 배치
            for meteo, dy in meteos: scr.blit(meteo[0], meteo[1])
            for atk in atks: scr.blit(atk_img, atk)
            scr.blit(plane_img, plane)
            for crush in bang:
                
                scr.blit(crush_img, crush)
                if cnt >= 2:
                    
                    bang.remove(crush)
                    cnt = 0

            score_image = small_font.render('SCORE {}'.format(score), True, YELLOW)
            scr.blit(score_image, (10, 10))

            life_image = small_font.render('{}'.format(health_cnt), True, WHITE)
            scr.blit(life_image, (scr_width - 60, 10))
            scr.blit(health_img, (scr_width - 120, 20))
            
            cnt += 0.1                              # 충돌 이미지 삭제를 위한 카운트

            go_img = small_font.render('GAME OVER', True, RED)
            if gameover: scr.blit(go_img, go_img.get_rect(centerx = scr_width/2, centery = scr_height/2))

        pg.display.update()
        clk.tick(30)
    
    except: break