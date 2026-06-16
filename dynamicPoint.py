import math
from constants import *
class dynamicPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.coord = (x, y)

    def translate(self, dx, dy):
        translated = dynamicPoint(self.x+dx, self.y+dy)
        return translated
    
    def rotate(self, theta):
        #first convert degrees to radians : 360 deg = 2pi rad, 180 deg = pi rad, deg/180 = pirad / 180
        radians = theta*math.pi/180

        sine = math.sin(radians)
        cosine = math.cos(radians)

        rx = cosine*self.x - sine*self.y
        ry = sine*self.x + cosine*self.y

        rotated = dynamicPoint(rx, ry)
        return rotated
    
    def scale(self, factor):
        sx = self.x*factor
        sy = self.y*factor

        scaled = dynamicPoint(sx, sy)
        return scaled