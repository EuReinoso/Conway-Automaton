import pygame,sys
from numpy import empty
from individual import Individual

pygame.init()

BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
YELLOW = (200, 200, 0)

WINDOW_SIZE = (640, 480)
TILE_SIZE = 8

screen = pygame.Surface(WINDOW_SIZE)

grid_list = empty(shape=[round(WINDOW_SIZE[0]/TILE_SIZE), round(WINDOW_SIZE[1]/TILE_SIZE)], 
                        dtype= object)

fps = 60
time = pygame.time.Clock()

w = WINDOW_SIZE[0]//len(grid_list)
h = WINDOW_SIZE[1]//len(grid_list[0])

start = False

def click(pos,state):
    i = pos[1]//w
    j = pos[0]//h

    grid_list[j][i].alive = state

def pause():
    global start,fps
    if start:
        fps = 60
        start = False
    else:
        fps = 10
        start = True

def gen_rects():
    x = 0
    for i in range(0,screen.get_size()[0],TILE_SIZE):
        y = 0
        for j in range(0, screen.get_size()[1], TILE_SIZE):
            rect = pygame.Rect(i, j, TILE_SIZE, TILE_SIZE)
            grid_list[x, y] = Individual(rect)
            y += 1
        x += 1

def draw_grid():
    for line in grid_list:
        for idv in line:
            if idv.alive:
                pygame.draw.rect(screen, YELLOW, idv.rect)

                
            # else:
            #     pygame.draw.rect(screen, WHITE, idv.rect, 1)

def gen_adjacents():
    x = 0
    for line in grid_list:
        y = 0
        for idv in line:
            if x > 0:
                idv.adjacents.append(grid_list[x - 1][y])
            if x < len(grid_list) - 1:
                idv.adjacents.append(grid_list[x + 1][y])
            if y > 0:
                idv.adjacents.append(grid_list[x][y - 1])
            if y < len(line) - 1:
                idv.adjacents.append(grid_list[x][y + 1])

            if x > 0 and y > 0:
                idv.adjacents.append(grid_list[x - 1][y - 1])
            if x < len(grid_list) - 1 and y < len(line) - 1:
                idv.adjacents.append(grid_list[x + 1][y + 1])
            if x > 0 and y < len(line) - 1:
                idv.adjacents.append(grid_list[x - 1][y + 1])
            if x < len(grid_list) - 1 and y > 0:
                idv.adjacents.append(grid_list[x + 1][y - 1])
            y += 1
        x += 1

def grid_is_alive():
    global grid_list
    array = []
    i = 0
    for line in grid_list:
        j = 0
        for idv in line:
            array.append(grid_list[i][j].is_alive()) 
            j+=1
        i+=1

    x = 0
    i = 0
    for line in grid_list:
        j = 0
        for idv in line:
            grid_list[i][j].alive = array[x]
            j+=1
            x+=1
        i+=1

def clean():
    i = 0
    for line in grid_list:
        j = 0
        for idv in line:
            grid_list[i][j].alive = False
            j+=1
        i+=1
    

window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('Conways Game')

gen_rects()
gen_adjacents()

while True:

    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:    
                pause()
            if event.key == pygame.K_c:
                clean()
        if event.type == pygame.MOUSEBUTTONUP:
            if pygame.mouse.get_pressed(3)[0]:
                click(pygame.mouse.get_pos(),True)
            if pygame.mouse.get_pressed(3)[2]:
                click(pygame.mouse.get_pos(),False)

        if event.type == pygame.MOUSEMOTION:
            if pygame.mouse.get_pressed(3)[0]:
                click(pygame.mouse.get_pos(),True)
            if pygame.mouse.get_pressed(3)[2]:
                click(pygame.mouse.get_pos(),False)
        
    if start:
        grid_is_alive()

    draw_grid()
    window.blit(screen,(0, 0))
    pygame.display.update()
    time.tick(fps)