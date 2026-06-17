import pygame
import random
from Player import *
from constants import *
from cell import *
import levels


pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill("black")
pygame.display.flip()




cells = []

#push cells away from each other

def cell_push_apart():
    for this in cells:
        for other in cells:
            if other != this:
                #find distance, ux, uy
                dx = other.x-this.x
                dy = other.y-this.y
                distance = math.sqrt(dx**2 + dy**2)
                if distance<5:
                    distance = 5
                if distance < this.radius+other.radius:
                    ux = dx/distance
                    uy = dy/distance
                    overlap = other.radius + this.radius - distance
                    fx = this.x - ux*overlap
                    fy = this.y - uy*overlap
                    
                    this.x += (fx-this.x)/4
                    this.y += (fy-this.y)/4
                
        #check collision with player
        dx = player.x-this.x
        dy = player.y-this.y
        distance = math.sqrt(dx**2 + dy**2)
        if distance<5:
            distance = 5
        if distance < this.radius+other.radius:
            ux = dx/distance
            uy = dy/distance
            overlap = 50 + this.radius - distance
            fx = this.x - ux*overlap
            fy = this.y - uy*overlap 
            this.x += (fx-this.x)/4
            this.y += (fy-this.y)/4










def update_cells():
    for cell in cells:
        cell.update()
        cell.draw(screen)
        
def new_cell(x, y, r):
    new = cell(x, y, r)
    cells.append(new)

def createCellBox():
        widthLow = -200
        widthHigh = 1000
        heightLow = -200
        heightHigh = 1000
        for i in range(widthLow, widthHigh, 40):
            new_cell(widthLow+random.randint(-10, 10), i+random.randint(-10, 10), random.randint(30, 50))
            new_cell(widthHigh+random.randint(-10, 10), i+random.randint(-10, 10), random.randint(30, 50))
        for i in range(heightLow, heightHigh, 40):
            new_cell(i+random.randint(-10, 10), heightLow+random.randint(-10, 10), random.randint(30, 50))
            new_cell(i+random.randint(-10, 10), heightHigh+random.randint(-10, 10), random.randint(30, 50))
        

        for i in range(50):
            pass
        





player = Player(CENTER_X+100, CENTER_Y)
l1 = levels.one()
l2 = levels.two()
l3 = levels.three()
l4 = levels.four()
l5 = levels.five()

#render player image
player_image = pygame.image.load("/Users/enzogleichauf/Documents/whitebloodcell.png")
def render_player():
    img_width = 100
    img_height = 100

    transformed = pygame.transform.scale(player_image, (img_width, img_height))
    screen.blit(transformed, (player.point.x-img_width/2, player.point.y-img_width/2))

createCellBox()
clock = pygame.time.Clock()
running = True
time = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    clock.tick(60)
    screen.fill("white")
    player.draw(screen)

    render_player()

    player.update_controls()
    update_cells()
    cell_push_apart()
    
    pygame.display.flip()
    

pygame.quit()

