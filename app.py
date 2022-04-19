import pygame
from pygame.display import flip

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768
BG_COLOR = (255, 255, 255)

clock = pygame.time.Clock()

# Initialize Pygame
pygame.init()

def create_main_surface():
    # Tuple representing width and height in pixels
    screen_size = (SCREEN_WIDTH, SCREEN_HEIGHT)

    # Create window with given size
    return pygame.display.set_mode(screen_size)

def render_frame(surface, state):
    clear_surface(surface, BG_COLOR) # render the frame
    state.render(surface)
    flip()

def clear_surface(surface, color):
    surface.fill(color)

class State:
    def __init__(self):
        self.x = 0

    def updateX(self, d_t): 
        self.x += 20*d_t # update circle position based on its velocity and d_t

    def render(self, surface):  
        pygame.draw.circle(surface, (0,0,0), (self.x, SCREEN_HEIGHT/2), 100, 10)


def main():
    surface = create_main_surface()

    state = State()

    running = True
    while (running == True):
        d_t = clock.tick()/1000 # update the clock and get time since the last call of .tick()

        for e in pygame.event.get():
            if (e.type == pygame.KEYDOWN): 
                print ("u win")
            if (e.type == pygame.QUIT):
                running = False
        state.updateX(d_t)
        render_frame(surface, state)    
    
main()