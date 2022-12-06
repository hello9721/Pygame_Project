# Screen Value
SCRWIDTH = 500
SCRHEIGHT = 700

# game options/settings
FONT_NAME = 'arial'
HS_FILE = "highscore.txt"

TITLE = "Endless Jump"
KEY_REPEAT_1 = 100
KEY_REPEAT_2 = 10
FPS = 40
START_X = 20
START_Y = SCRHEIGHT - 20

# Starting platforms
PLATFORM_LIST = [(0, SCRHEIGHT - 60),
                 (SCRWIDTH/2 - 50, SCRHEIGHT*3/4),
                 (125, SCRHEIGHT - 350),
                 (350, 200),
                 (175, 100)]


# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
LIGHTBLUE = (0, 155, 155)
BGCOLOR = LIGHTBLUE

# Ball Value
WIDTH = 50
HEIGHT = 50
VEL = 3
JUMP_HEIGHT = 11

# Platform Value
P_WIDTH_1 = 50      # 랜덤 범위 최소
P_WIDTH_2 = 250     # 랜덤 범위 최대
P_HEIGHT = 50
NUM_PLAT = 6