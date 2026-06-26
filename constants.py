import pygame
from pyvidplayer2 import Video

pygame.init()

WIDTH = 1200
HEIGHT = 675
CENTER_X = WIDTH/2
CENTER_Y = HEIGHT/2

#game engine components
SCROLL_X = 0
SCROLL_Y = 0
DIRECTION = 0 # in degrees
ZOOM = 1 #in times scale
SCORE = 0

#graphics assets
RETICLE = pygame.image.load("./reticle.png")

MIDDLEGROUND_IMG = pygame.image.load("./level1mg.png")

CELL_NORMAL = pygame.image.load("./cell1.png")
CELL_RED = pygame.image.load("./cell_red.png")

PLAYER_IMAGE = pygame.image.load("./player.png")

#player settings
PLAYER_SPEED = 1

#text assets

GAME_FONT = pygame.font.Font("./GoogleSans-VariableFont_GRAD,opsz,wght.ttf", 50)

#video assets

OPENING_CUTSCENE = Video("./cancergameopening_resized.mp4")


