import pygame as pg
import random as rd

pg.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 700

scr = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clk = pg.time.Clock() 

score = 0
small_font = pg.font.SysFont('malgungothic', 30)

# 과일 이미지
blue_img = pg.image.load('./assets/p_grape.png')
orange_img = pg.image.load('./assets/o_orange.png')
red_img = pg.image.load('./assets/r_apple.png')
yellow_img = pg.image.load('./assets/y_banana.png')

blue_img = pg.transform.scale(blue_img, (90, 90))
orange_img = pg.transform.scale(orange_img, (90, 90))
red_img = pg.transform.scale(red_img, (90, 90))
yellow_img = pg.transform.scale(yellow_img, (90, 90))

fruits = [blue_img, orange_img, red_img, yellow_img]

# 체력바 이미지
health_3 = pg.image.load('./assets/health_full.png')
health_2 = pg.image.load('./assets/health_2.png')
health_1 = pg.image.load('./assets/health_1.png')
health_0 = pg.image.load('./assets/health_0.png')

health = 3

# 바스켓 이미지
bsk_l = pg.image.load('./assets/y_basket.png')
bsk_r = pg.image.load('./assets/p_basket.png')
bsk_u = pg.image.load('./assets/r_basket.png')
bsk_d = pg.image.load('./assets/o_basket.png')

bsk_l = pg.transform.scale(bsk_l, (100, 100))
bsk_r = pg.transform.scale(bsk_r, (100, 100))
bsk_u = pg.transform.scale(bsk_u, (100, 100))
bsk_d = pg.transform.scale(bsk_d, (100, 100))

bsk_l_rect = bsk_l.get_rect(centery = ((SCREEN_HEIGHT-100)/2), left = 48)
bsk_r_rect = bsk_r.get_rect(centery = ((SCREEN_HEIGHT-100)/2), right = SCREEN_WIDTH-47)
bsk_u_rect = bsk_u.get_rect(centerx = SCREEN_WIDTH/2, top = 47)
bsk_d_rect = bsk_d.get_rect(centerx = SCREEN_WIDTH/2, bottom = SCREEN_HEIGHT-147)

# 안내판 이미지
circle_b = pg.image.load('./assets/circle_b.png')
circle_t = pg.image.load('./assets/circle_t.png')
circle_bg = pg.image.load('./assets/circle_bg.png')

circle_b = pg.transform.scale(circle_b, (420, 420))
circle_t = pg.transform.scale(circle_t, (438, 438))
circle_bg = pg.transform.scale(circle_bg, (550, 550))

# 메인 과일 이미지
fruit_img = [fruits[rd.randint(0, len(fruits) - 1)], fruits[rd.randint(0, len(fruits) - 1)], fruits[rd.randint(0, len(fruits) - 1)], fruits[rd.randint(0, len(fruits) - 1)]]
fruit = fruit_img[0].get_rect(centery = ((SCREEN_HEIGHT-100)/2), centerx = SCREEN_WIDTH/2)

next_furit_img_1 = pg.transform.scale(fruit_img[1], (50, 50))
next_furit_1 = next_furit_img_1.get_rect(top = SCREEN_HEIGHT - 50, right = SCREEN_WIDTH - 120)
next_furit_img_2 = pg.transform.scale(fruit_img[2], (50, 50))
next_furit_2 = next_furit_img_2.get_rect(top = SCREEN_HEIGHT - 50, right = SCREEN_WIDTH - 60)
next_furit_img_3 = pg.transform.scale(fruit_img[2], (50, 50))
next_furit_3 = next_furit_img_3.get_rect(top = SCREEN_HEIGHT - 50, right = SCREEN_WIDTH - 10)

head, angle = "top", 0

# circle_l 90.0 yellow
# circle_b 180.0 orange
# circle_r 270.0 blue
# circle_t 360.0 red

bg_img = pg.image.load('./assets/bg.png')

# 게임오버 화면
gameover = pg.image.load('./assets/gameover.png')
gameover = pg.transform.scale(gameover, (600, 700))

go = False

while True:

    try:

        if not go:
            for event in pg.event.get():

                if event.type == pg.QUIT:
                    break

                if event.type == pg.KEYDOWN:

                    if event.key == pg.K_LEFT:

                        head = "left"
                        n = 90 - angle
                        angle = 90

                        circle_t = pg.transform.rotate(circle_t, n)

                        if fruit_img[0] == yellow_img:

                            score += 100

                            fruit_img.pop(0)
                            fruit_img.append(fruits[rd.randint(0, len(fruits) - 1)])
                            fruit = fruit_img[0].get_rect(centery = ((SCREEN_HEIGHT-100)/2), centerx = SCREEN_WIDTH/2)

                            next_furit_img_1 = pg.transform.scale(fruit_img[1], (50, 50))
                            next_furit_1 = next_furit_img_1.get_rect(top = SCREEN_HEIGHT - 50, right = SCREEN_WIDTH - 120)
                            next_furit_img_2 = pg.transform.scale(fruit_img[2], (50, 50))
                            next_furit_2 = next_furit_img_2.get_rect(top = SCREEN_HEIGHT - 50, right = SCREEN_WIDTH - 60)
                            next_furit_img_3 = pg.transform.scale(fruit_img[2], (50, 50))
                            next_furit_3 = next_furit_img_3.get_rect(top = SCREEN_HEIGHT - 50, right = SCREEN_WIDTH - 10)
                        
                        else:
                            
                            score -= 200
                            health -= 1
                    
                    elif event.key == pg.K_RIGHT:

                        head = "right"
                        n = (-1 * 90) - angle
                        angle = -1 * 90

                        circle_t = pg.transform.rotate(circle_t, n)

                        if fruit_img[0] == blue_img:

                            score += 100

                            fruit_img.pop(0)
                            fruit_img.append(fruits[rd.randint(0, len(fruits) - 1)])
                            fruit = fruit_img[0].get_rect(centery = ((SCREEN_HEIGHT-100)/2), centerx = SCREEN_WIDTH/2)

                            next_furit_img_1 = pg.transform.scale(fruit_img[1], (50, 50))
                            next_furit_1 = next_furit_img_1.get_rect(top = SCREEN_HEIGHT - 50, right = SCREEN_WIDTH - 120)
                            next_furit_img_2 = pg.transform.scale(fruit_img[2], (50, 50))
                            next_furit_2 = next_furit_img_2.get_rect(top = SCREEN_HEIGHT - 50, right = SCREEN_WIDTH - 60)
                            next_furit_img_3 = pg.transform.scale(fruit_img[2], (50, 50))
                            next_furit_3 = next_furit_img_3.get_rect(top = SCREEN_HEIGHT - 50, right = SCREEN_WIDTH - 10)
                            
                        else:
                            
                            score -= 200
                            health -= 1

                    elif event.key == pg.K_DOWN:

                        head = "down"
                        n = 180 - angle
                        angle = 180

                        circle_t = pg.transform.rotate(circle_t, n)

                        if fruit_img[0] == orange_img:

                            score += 100

                            fruit_img.pop(0)
                            fruit_img.append(fruits[rd.randint(0, len(fruits) - 1)])
                            fruit = fruit_img[0].get_rect(centery = ((SCREEN_HEIGHT-100)/2), centerx = SCREEN_WIDTH/2)

                            next_furit_img_1 = pg.transform.scale(fruit_img[1], (50, 50))
                            next_furit_1 = next_furit_img_1.get_rect(top = SCREEN_HEIGHT - 50, right = SCREEN_WIDTH - 120)
                            next_furit_img_2 = pg.transform.scale(fruit_img[2], (50, 50))
                            next_furit_2 = next_furit_img_2.get_rect(top = SCREEN_HEIGHT - 50, right = SCREEN_WIDTH - 60)
                            next_furit_img_3 = pg.transform.scale(fruit_img[2], (50, 50))
                            next_furit_3 = next_furit_img_3.get_rect(top = SCREEN_HEIGHT - 50, right = SCREEN_WIDTH - 10)
                            
                        else:
                            
                            score -= 200
                            health -= 1

                    elif event.key == pg.K_UP:

                        head = "top"
                        n = 0 - angle
                        angle = 0

                        circle_t = pg.transform.rotate(circle_t, n)

                        if fruit_img[0] == red_img:

                            score += 100

                            fruit_img.pop(0)
                            fruit_img.append(fruits[rd.randint(0, len(fruits) - 1)])
                            fruit = fruit_img[0].get_rect(centery = ((SCREEN_HEIGHT-100)/2), centerx = SCREEN_WIDTH/2)

                            next_furit_img_1 = pg.transform.scale(fruit_img[1], (50, 50))
                            next_furit_1 = next_furit_img_1.get_rect(top = SCREEN_HEIGHT - 50, right = SCREEN_WIDTH - 120)
                            next_furit_img_2 = pg.transform.scale(fruit_img[2], (50, 50))
                            next_furit_2 = next_furit_img_2.get_rect(top = SCREEN_HEIGHT - 50, right = SCREEN_WIDTH - 60)
                            next_furit_img_3 = pg.transform.scale(fruit_img[2], (50, 50))
                            next_furit_3 = next_furit_img_3.get_rect(top = SCREEN_HEIGHT - 50, right = SCREEN_WIDTH - 10)
                            
                        else:
                            
                            score -= 200
                            health -= 1

                    elif event.key == pg.K_ESCAPE: pg.quit() 

            score_img = small_font.render('SCORE {}'.format(score), True, (255, 255, 255))
            health_img = small_font.render('LIFE', True, (255, 255, 255))

            if health == 3: life_img = health_3
            elif health == 2: life_img = health_2
            elif health == 1: life_img = health_1
            elif health <= 0: life_img = health_0

            if health <= 0:

                go = True

            scr.blit(bg_img, (0, 0))
            scr.blit(circle_bg, (25, 25))

            scr.blit(bsk_d, bsk_d_rect)
            scr.blit(bsk_u, bsk_u_rect)
            scr.blit(bsk_l, bsk_l_rect)
            scr.blit(bsk_r, bsk_r_rect)

            scr.blit(circle_b, (90, 90))
            scr.blit(circle_t, (81, 81))

            scr.blit(fruit_img[0], fruit)
            scr.blit(next_furit_img_1, next_furit_1)
            scr.blit(next_furit_img_2, next_furit_2)
            scr.blit(next_furit_img_3, next_furit_3)
            scr.blit(score_img, (15, SCREEN_HEIGHT - 90))
            scr.blit(health_img, (SCREEN_WIDTH - 145 - health_img.get_width(), SCREEN_HEIGHT - 90))
            scr.blit(life_img, (SCREEN_WIDTH - 135, SCREEN_HEIGHT - 90))

        else :

            scr.blit(bg_img, (0, 0))
            scr.blit(circle_bg, (25, 25))

            scr.blit(bsk_d, bsk_d_rect)
            scr.blit(bsk_u, bsk_u_rect)
            scr.blit(bsk_l, bsk_l_rect)
            scr.blit(bsk_r, bsk_r_rect)

            scr.blit(circle_b, (90, 90))
            scr.blit(circle_t, (81, 81))

            scr.blit(fruit_img[0], fruit)
            scr.blit(next_furit_img_1, next_furit_1)
            scr.blit(next_furit_img_2, next_furit_2)
            scr.blit(next_furit_img_3, next_furit_3)
            scr.blit(score_img, (15, SCREEN_HEIGHT - 90))
            scr.blit(health_img, (SCREEN_WIDTH - 145 - health_img.get_width(), SCREEN_HEIGHT - 90))
            scr.blit(life_img, (SCREEN_WIDTH - 135, SCREEN_HEIGHT - 90))

            score_rect = score_img.get_rect(centerx = SCREEN_WIDTH/2, centery = SCREEN_HEIGHT/2)

            scr.blit(gameover, (0, 0))
            scr.blit(score_img, score_rect)

            event = pg.event.poll()
            if event.type == pg.QUIT: pg.quit()

        pg.display.update()
        clk.tick(30)

    except:
    
        pg.quit()
        break