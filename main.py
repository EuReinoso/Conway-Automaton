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

window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('Conways Game')

gen_rects()
while True:

    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    draw_grid()
    window.blit(screen,(0, 0))
    pygame.display.update()