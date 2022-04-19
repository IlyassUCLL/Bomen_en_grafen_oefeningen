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

def process_key_input(state, d_t, key):
    if key[pygame.K_LEFT]:
        state.updateX(d_t, -1)

    if key[pygame.K_UP]:
        state.updateY(d_t, 1)    

    if key[pygame.K_RIGHT]:
        state.updateX(d_t, 1)

    if key[pygame.K_DOWN]:
        state.updateY(d_t, -1)    
def render_frame(surface, state):
    clear_surface(surface, BG_COLOR) # render the frame
    state.render(surface)
    flip()

def clear_surface(surface, color):
    surface.fill(color)

class State:
    def __init__(self):
        self.x = 0
        self.y = 0

    def updateX(self, d_t, dir): 
        self.x += dir*500*d_t # update circle position based on its velocity and d_t

    def updateY(self, d_t, dir): 
        self.y += -dir*500*d_t # update circle position based on its velocity and d_t    

    def render(self, surface):  
        pygame.draw.circle(surface, (0,0,0), (self.x, self.y), 100, 10)


def main():
    surface = create_main_surface()
    state = State()
    running = True
    
    while (running == True):
        d_t = clock.tick()/1000 # update the clock and get time since the last call of .tick()

        for e in pygame.event.get():
            if (e.type == pygame.QUIT):
                running = False

        process_key_input(state, d_t, pygame.key.get_pressed())
        render_frame(surface, state)    
    
main()