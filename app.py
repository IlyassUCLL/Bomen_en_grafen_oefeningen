import pygame
from pygame.display import flip
from time import sleep

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768

clock = pygame.time.Clock()

# Initialize Pygame
pygame.init()

def create_main_surface():
    # Tuple representing width and height in pixels
    screen_size = (SCREEN_WIDTH, SCREEN_HEIGHT)

    # Create window with given size
    return pygame.display.set_mode(screen_size)

def render_frame(surface, x):
    pygame.draw.circle(surface, (0,0,0), (x, SCREEN_HEIGHT/2), 100, 0)
    flip()

def clear_surface(surface, color):
    surface.fill(color)



def main():
    surface = create_main_surface()

    circle_x = 0

    running = True
    while (running == True):
        d_t = clock.tick()/1000 # update the clock and get time since the last call of .tick()
        clear_surface(surface, (255,255,255))

        circle_x += 20*d_t # update circle position based on its velocity and d_t

        render_frame(surface,  circle_x) # render the frame

        for e in pygame.event.get():
            if (e.type == pygame.KEYDOWN): 
                print ("u win")
            if (e.type == pygame.QUIT):
                running = False
    
main()