import pygame
import math
import random

WIDTH = 800
HEIGHT = 800
CENTER_X = WIDTH/2
CENTER_Y = HEIGHT/2

#game engine components
SCROLL_X = 0
SCROLL_Y = 0

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill("black")
pygame.display.flip()




class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.forward_speed = 0
        self.direction = 0

        self.dev_shape = pygame.Rect(self.x-20, self.y-30, 40, 60)
    def draw(self):
        pygame.draw.rect(screen, "red", self.dev_shape, 2)
        pygame.draw.line(screen, "red", (self.dev_shape.left, self.dev_shape.top), (self.dev_shape.right, self.dev_shape.bottom))





















player = Player(CENTER_X, CENTER_Y)

clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    clock.tick(60)
    screen.fill("white")
    player.draw()
    pygame.display.flip()


pygame.quit()









