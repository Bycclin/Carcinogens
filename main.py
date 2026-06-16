
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
                    overlap = abs(other.radius-this.radius)
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
            overlap = abs(50-this.radius)
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
        for i in range(-200, 1000, 40):
            new_cell(-200+random.randint(-10, 10), i+random.randint(-10, 10), random.randint(30, 50))
            new_cell(1000+random.randint(-10, 10), i+random.randint(-10, 10), random.randint(30, 50))
        for i in range(-200, 1000, 40):
            new_cell(i+random.randint(-10, 10), -200+random.randint(-10, 10), random.randint(30, 50))
            new_cell(i+random.randint(-10, 10), 1000+random.randint(-10, 10), random.randint(30, 50))
        


new_cell(CENTER_X, 50, 30)
new_cell(50, CENTER_Y, 50)


player = Player(CENTER_X+100, CENTER_Y)
l1 = levels.one()
l2 = levels.two()
l3 = levels.three()
l4 = levels.four()
l5 = levels.five()



createCellBox()
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    clock.tick(60)
    screen.fill("white")
    player.draw(screen)
    player.update_controls()
    update_cells()
    cell_push_apart()
    
    pygame.display.flip()


pygame.quit()

