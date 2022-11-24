import pygame as pg

# 색상표
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
YELLOW = (255, 255, 0)

pg.init()                               # 초기화
scr = pg.display.set_mode((800,800))    # 화면 크기 설정 및 변수 저장
clk = pg.time.Clock()                   # FPS 함수 변수 저장

smp_img = pg.image.load("./ball.png")   # 이미지를 불러와 변수에 저장
smp_img = pg.transform.scale(smp_img, (80, 80))
                                        # 이미지 크기 조정

while 1:                                # 메인 루프

    scr.fill(BLACK)                     # 화면 배경색 채우기

    event = pg.event.poll()             # 단일 이벤트 반환
    if event.type == pg.QUIT: break     # 루프 중지 조건문

    scr.blit(smp_img, (400 - smp_img.get_width() / 2, 800 - smp_img.get_height()))
                                        # 해당 위치에 이미지 그리기

    pg.display.update()                 # 전체 화면 업데이트
    clk.tick(30)                        # FPS = 30

pg.quit()                               # 종료