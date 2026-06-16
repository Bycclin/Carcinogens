import pygame
from dynamicPoint import *
from constants import *
class cell:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.point = dynamicPoint(self.x, self.y)
        
    
    def draw(self, screen):
        pygame.draw.circle(screen, "blue", (self.point.x, self.point.y), self.radius*ZOOM, 2)
        pygame.draw.line(screen, "blue", (self.point.x+0.7011*self.radius*ZOOM, self.point.y+0.7011*self.radius*ZOOM), (self.point.x-0.7011*self.radius*ZOOM, self.point.y-0.7011*self.radius*ZOOM), 2)
        pygame.draw.line(screen, "blue", (self.point.x-0.7011*self.radius*ZOOM, self.point.y+0.7011*self.radius*ZOOM), (self.point.x+0.7011*self.radius*ZOOM, self.point.y-0.7011*self.radius*ZOOM), 2)

    def update(self):
        self.point.x = self.x
        self.point.y = self.y
        
        
        
       
        #offset based off scroll
        self.point = self.point.translate(-SCROLL_X, -SCROLL_Y)
        