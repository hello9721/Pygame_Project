import pygame

pygame.init()                            # 처음에 적고 시작!

background = pygame.display.set_mode((480, 360))  # 가로 세로
pygame.display.set_caption("GAME")       # 창 제목

fps = pygame.time.Clock()                # 게임의 빠르기

# 중심
x_pos = background.get_size()[0]//2      # 480 // 2
y_pos = background.get_size()[1]//2      # 360 // 2

to_x = 0
to_y = 0

play = True
while play:
   deltaTime = fps.tick(60)              # 1초에 몇번?
   for event in pygame.event.get():      # 발생하는 이벤트
      if event.type == pygame.QUIT:      # 종료하고 싶다면
         play = False
      if event.type == pygame.KEYDOWN:   # 키보드 입력값을 아스키코드로 변환
         if event.key == pygame.K_UP:
            to_y = -1
         elif event.key == pygame.K_DOWN:
            to_y = 1
         elif event.key == pygame.K_RIGHT:
            to_x = 1
         elif event.key == pygame.K_LEFT:
            to_x = -1
      elif event.type == pygame.KEYUP:   
         if event.key == pygame.K_UP:
            to_y = 0
         elif event.key == pygame.K_DOWN:
            to_y = 0
         elif event.key == pygame.K_RIGHT:
            to_x = 0
         elif event.key == pygame.K_LEFT:
            to_x = 0

   x_pos += to_x                         # 누적 x
   y_pos += to_y                         # 누적 y

   # 순서 중요 !! 배경 >> 점찍기 / while 안에 넣어야 바뀌는게 계속 반영
   background.fill((255,255,255))        # 배경
   pygame.draw.circle(background, (0,0,255), (x_pos, y_pos), 5)
   # pygame.draw.circle(surface, color, center, radius)
   pygame.display.update()               # 설정 반영

pygame.quit()