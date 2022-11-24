import pygame as pg
import random as rd

pg.init()

scr_width = 600
scr_height = 900

scr = pg.display.set_mode((scr_width, scr_height))
clk = pg.time.Clock() 

bg_img = pg.image.load('bg.png')            # 배경 이미지 설정

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

for i in range(5):                          # 소환할 운석들 사이즈, 속도 랜덤으로 생성

    n = rd.randint(0, 1)
    meteo = meteo_size[n].get_rect(top = -100)
    meteo.left = rd.randint(0, scr_width - meteo_size[n].get_width())

    dy = rd.randint(5, 12)
    
    meteos.append(((meteo_size[n], meteo), dy))

while True:

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

            n = rd.randint(0, 1)
            meteo = meteo_size[n].get_rect(top = -100)
            meteo.left = rd.randint(0, scr_width - meteo_size[n].get_width())

            dy = rd.randint(5, 12)
            
            meteos.append(((meteo_size[n], meteo), dy))
    
    for atk in atks:                        # 미사일 날리기

        atk.top -= 6
        if atk.top < 0: atks.remove(atk)


    if plane.left < 0: plane.left = 0       # 비행기 스크린 밖으로 나가지 않도록 벽처리
    elif plane.right > 600: plane.right = 600
    elif plane.bottom > 900: plane.bottom = 900
    elif plane.top < 0: plane.top = 0

    scr.blit(bg_img, (0, 0))
    for meteo, dy in meteos: scr.blit(meteo[0], meteo[1])
    for atk in atks: scr.blit(atk_img, atk)
    scr.blit(plane_img, plane)

    pg.display.update()
    clk.tick(30)