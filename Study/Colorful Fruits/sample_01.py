import pygame as pg

pg.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

scr = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clk = pg.time.Clock() 

# 과일 이미지
blue_img = pg.image.load('./assets/b_blueberry.png')
orange_img = pg.image.load('./assets/o_orange.png')
red_img = pg.image.load('./assets/r_peach.png')
yellow_img = pg.image.load('./assets/y_pineapple.png')

# 바스켓 이미지
bsk_img = pg.image.load('./assets/basket.png')
bsk_img = pg.transform.scale(bsk_img, (100, 100))

bsk_r = bsk_img.get_rect(centery = SCREEN_HEIGHT/2, left = 25)
bsk_l = bsk_img.get_rect(centery = SCREEN_HEIGHT/2, right = SCREEN_WIDTH-25)
bsk_u = bsk_img.get_rect(centerx = SCREEN_WIDTH/2, top = 25)
bsk_d = bsk_img.get_rect(centerx = SCREEN_WIDTH/2, bottom = SCREEN_HEIGHT-25)

# 안내판 이미지
circle_b = pg.image.load('./assets/circle_b.png')
circle_b = pg.transform.scale(circle_b, (500, 500))
circle_t = pg.image.load('./assets/circle_t.png')
circle_t = pg.transform.scale(circle_t, (500, 500))

angle = 0

# circle_l 90.0 yellow
# circle_b 180.0 orange
# circle_r 270.0 blue
# circle_t 360.0 red

bg_img = pg.image.load('./assets/bg.png')

while True:


    for event in pg.event.get():
        if event.type == pg.QUIT:
            break

        if event.type == pg.KEYDOWN:

            if event.key == pg.K_LEFT:

                n = 90 - angle

                for i in range()

    scr.blit(bg_img, (0, 0))
    scr.blit(bsk_img, bsk_d)
    scr.blit(bsk_img, bsk_u)
    scr.blit(bsk_img, bsk_l)
    scr.blit(bsk_img, bsk_r)
    scr.blit(circle_b, (50, 50))
    scr.blit(circle_t, (50, 50))

    pg.display.update()
    clk.tick(30)

pg.quit() 
