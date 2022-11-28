import pygame
import sys

MAX_WIDTH = 800
MAX_HEIGHT = 400

def makePygame(name):
    pygame.init()
    pygame.display.set_caption(name)

    screen = pygame.display.set_mode((MAX_WIDTH, MAX_HEIGHT))
    fps = pygame.time.Clock()

    dinoImg1 = pygame.image.load('./assets/sample_ball.png')
    dinoImg2 = pygame.image.load('./assets/sample_ball.png')

    dinoImg1 = pygame.transform.scale(dinoImg1, (60, 60))
    dinoImg2 = pygame.transform.scale(dinoImg2, (70, 70))

    dinoHeight = dinoImg1.get_size()[1]
    dinoBottom = MAX_HEIGHT - dinoHeight

    dinoX = 60
    dinoY = dinoBottom
    jumpTop = 200

    legSwap = True
    isBottom = True
    isGoUp = False

    #tree
    blockImg = pygame.image.load('./assets/sample_ball.png')
    blockImg = pygame.transform.scale(blockImg, (40, 40))
    blockHeight = blockImg.get_size()[1]
    blockX = MAX_WIDTH
    blockY = MAX_HEIGHT - blockHeight

    while True:
        screen.fill((255, 255, 255))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if isBottom:
                    isGoUp = True
                    isBottom = False

        if isGoUp:
            dinoY -= 20.0
        elif not isGoUp and not isBottom:
            dinoY += 20.0

        if isGoUp and dinoY <= jumpTop:
            isGoUp = False

        if not isBottom and dinoY >= dinoBottom:
            isBottom = True
            dinoY = dinoBottom

        #dinosour
        if legSwap:
            screen.blit(dinoImg1, (dinoX, dinoY))
            legSwap = False
        else:
            screen.blit(dinoImg2, (dinoX, dinoY))
            legSwap = True

        #block
        blockX -= 10.0
        if blockX <=0:
            blockX = MAX_WIDTH

        screen.blit(blockImg, (blockX, blockY))

        pygame.display.update()
        fps.tick(10)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    makePygame('my pygame')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/