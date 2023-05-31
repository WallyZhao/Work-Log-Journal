import pygame
import os    # to define path to images

# basic pygame window
WIDTH, HEIGHT = 640, 640
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hexen")
FPS = 60
VELOCITY = 15
WORLD = {
    1 : pygame.image.load(os.path.join('sprites', 'forest.png')),
    2: pygame.image.load(os.path.join('sprites', 'castle.png')),
    3 : pygame.image.load(os.path.join('sprites', 'bossfight.png'))
}

x_var = 1
x = x_var

BORDER = pygame.Rect(1, 0, 1, HEIGHT)

# player model scale
PH, PW = (60, 60)
SH, SW = (60, 60)

# loading images 
PLAYER = pygame.image.load(os.path.join('sprites', 'player.png'))
PLAYER_MODEL = pygame.transform.scale(PLAYER, (PH, PW))    # scaling model sizes

SKELETON = pygame.image.load(os.path.join('sprites', 'skeleton.png'))
SKELE_MODEL = pygame.transform.scale(SKELETON, (SH, SW))

'''
TITLE = pygame.image.load(os.path.join('sprites', 'title.png'))
FOREST = pygame.image.load(os.path.join('sprites', 'forest.png'))
CASTLE = pygame.image.load(os.path.join('sprites', 'castle.png'))
BOSS_FIGHT = pygame.image.load(os.path.join('sprites', 'bossfight.png'))
'''

# player movement
def player_movement(keys_pressed, player):
    if keys_pressed[pygame.K_a]: #and player.x - VELOCITY > 0: # left 
        player.x -= VELOCITY
    if keys_pressed[pygame.K_d] and player.x + VELOCITY + player.width < WIDTH + 25: # right
        player.x += VELOCITY
    if keys_pressed[pygame.K_w] and player.y - (VELOCITY - 15) > 0 : # up
        player.y -= VELOCITY
    if keys_pressed[pygame.K_s] and player.y + VELOCITY + player.height < HEIGHT + 15: # down 
        player.y += VELOCITY

        
        

# main console
def main():
    
    player = pygame.Rect(300, 300, PH, PW)

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)        # making this for loop run 60 times per second (FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        if player.colliderect(BORDER):
            x = x_var + 1
            draw_window(player, x)
            
        # player movement 
        keys_pressed = pygame.key.get_pressed()
        player_movement(keys_pressed, player)
        draw_window(player)

        
               
    pygame.quit()

    
# draw function to update the window 
def draw_world(x):
    pass
    '''
    WIN.fill('white')
    WIN.blit(WORLD[x], (0, 0))    # to "draw" images on the screen,
    pygame.draw.rect(WORLD[x], (0), BORDER)
    pygame.display.update()
    '''
    
def draw_window(player, x):

    WIN.fill('white')
    WIN.blit(WORLD[x], (0, 0))    # to "draw" images on the screen,
    pygame.draw.rect(WORLD[x], (0), BORDER)
    
    WIN.blit(PLAYER_MODEL, (player.x, player.y))
    WIN.blit(SKELE_MODEL, (140, 200))
    pygame.display.update()

    



if __name__ == "__main__":
    main() 

