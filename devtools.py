import pygame
import constants
import random
from main import new_cell

class DevTool:
    def __init__(self):
        pass
    def createCellBox(self, width, height):
        for i in range(height*3):
            new_cell(0, random.randint(0, height), random.randint(20, 40))
            new_cell(width, random.randint(0, height), random.randint(20, 40))
        for i in range(width*3):
            new_cell(random.randint(0, width), 0, random.randint(20, 40))
            new_cell(random.randint(0, width), height, random.randint(20, 40))