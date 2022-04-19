import pygame
from pygame.display import flip

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768


# Initialize Pygame
pygame.init()

def create_main_surface():
    # Tuple representing width and height in pixels
    screen_size = (SCREEN_WIDTH, SCREEN_HEIGHT)

    # Create window with given size
    return pygame.display.set_mode(screen_size)

def render_frame(surface, x):
    pygame.draw.circle(surface, (50,50,50), (x, SCREEN_HEIGHT/2), 100, 0)
    flip()


def main():
    surface = create_main_surface()
    
    running = True
    while (running == True):

        render_frame(surface,  pygame.mouse.get_pos()[0])

        for e in pygame.event.get():
            
            if (e.type == pygame.KEYDOWN): 
                print ("u win")
                
            if (e.type == pygame.QUIT):
                running = False

main()