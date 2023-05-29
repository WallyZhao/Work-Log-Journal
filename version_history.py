import pygame 

# display parameters 
FPS = 60
TILE_SIZE = 35
WIDTH, HEIGHT = 10, 20
WIN = pygame.display.set_mode((WIDTH * TILE_SIZE, HEIGHT * TILE_SIZE))

pygame.display.set_caption('Tetrs')

# creating a grid
grid = [pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE) for x in range(WIDTH) for y in range(HEIGHT)]

def draw_window():
    [pygame.draw.rect(WIN, (40, 40, 40), i_rect, 1) for i_rect in grid]
    WIN.fill('black')
    pygame.display.update(grid)

def main():
    clock = pygame.time.Clock()
    run = True 
    while run:
        clock.tick(FPS) 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False 
        
        draw_window(grid)

    pygame.quit

if __name__ == "__main__":
    main()
