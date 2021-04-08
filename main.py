import pygame,sys
from numpy import empty
from individual import Individual

pygame.init()

BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
YELLOW = (200, 200, 0)

WINDOW_SIZE = (640, 480)
TILE_SIZE = 15

screen = pygame.Surface(WINDOW_SIZE)

grid_list = empty(shape=[round(WINDOW_SIZE[0]/TILE_SIZE), round(WINDOW_SIZE[1]/TILE_SIZE)], 
                        dtype= object)

fps = 10
time = pygame.time.Clock()

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
            else:
                pygame.draw.rect(screen, WHITE, idv.rect, 1)

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
    for line in grid_list:
        for idv in line:
            idv.is_alive()

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

    grid_is_alive()

    draw_grid()
    window.blit(screen,(0, 0))
    pygame.display.update()
    time.tick(fps)