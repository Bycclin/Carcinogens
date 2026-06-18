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
    for i in range(len(cells)-1, -1, -1):
        this = cells[i]
        this.update()
        #this.draw(screen)
        render_cell(this.point.x, this.point.y, this.radius, this.ID*3, False)

def check_cell_kill():
    pos = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()[0]
    mouse_x = pos[0]
    mouse_y = pos[1]
    for i in range(len(cells)-1, -1, -1):
        
        this = cells[i]
        dx = this.x-mouse_x
        dy = this.y-mouse_y
        distance = math.sqrt(dx**2+dy**2)
        if distance<this.radius:
            render_cell(this.point.x, this.point.y, this.point.radius, this.point.ID, True)
            if mouse_pressed:
                #kill cell
                del cells[i]
        
def new_cell(x, y, r):
    new = cell(x, y, r)
    new.ID = len(cells)
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
        

        #for i in range(50):
        #    pass
        





player = Player(CENTER_X+100, CENTER_Y)
l1 = levels.one()
l2 = levels.two()
l3 = levels.three()
l4 = levels.four()
l5 = levels.five()

#render player image
PLAYER_IMAGE = pygame.image.load("./whitebloodcell.png")
def render_player():
    
    img_width = 100
    img_height = 100

    transformed = pygame.transform.scale(PLAYER_IMAGE, (img_width, img_height))
    screen.blit(transformed, (player.point.x-img_width/2, player.point.y-img_width/2))

CELL_NORMAL = pygame.image.load("./costume2.png")
CELL_RED = pygame.image.load("./red (1).png")
def render_cell(x, y, r, id, highlight : bool):
    
    img_width = 100
    img_height = 100

    if highlight:
        CELL_IMAGE = CELL_RED
    else:
        CELL_IMAGE = CELL_NORMAL

    transformed = pygame.transform.scale(CELL_IMAGE, (img_width, img_height))
    transformed = pygame.transform.rotate(transformed, id)
    screen.blit(transformed, (x-r, y-r))
    

createCellBox()
clock = pygame.time.Clock()
running = True
time = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    clock.tick(1600)
    screen.fill("white")
    player.draw(screen)

    render_player()

    player.update_controls()
    update_cells()
    cell_push_apart()
    check_cell_kill()
    
    pygame.display.flip()
    

pygame.quit()
