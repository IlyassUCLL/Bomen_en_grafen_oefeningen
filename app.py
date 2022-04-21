import pygame
from pygame.display import flip
from spaceship import Spaceship
import Background
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

class PlayerController:

    def __init__(self, keyboard):
        self.keyboard = keyboard

    def get_arrow_key_dir(self):
        v = pygame.Vector2()
        if (self.keyboard.is_key_pressed(pygame.K_LEFT)):
            v.x += -1


        if (self.keyboard.is_key_pressed(pygame.K_UP)):
            v.y += -1  

        if (self.keyboard.is_key_pressed(pygame.K_RIGHT)):

            v.x += 1

        if (self.keyboard.is_key_pressed(pygame.K_DOWN)):
            v.y += 1
            # Keep player on the screen

        # returns vector 0 length zero if no key presses or normalized direction
        if (v.length() == 0):
            return pygame.Vector2(0,0)
        return v.normalize()
    
def render_frame(surface, state):
    clear_surface(surface, BG_COLOR) # render the frame
    state.render(surface)
    # image = pygame.image.load('ufo4.png')
    # surface.blit(image,(state.x-30, state.y-30))
    flip()

def clear_surface(surface, color):
    surface.fill(color)

class Keyboard:
    def is_key_pressed(self, key):
        return pygame.key.get_pressed()[key]
    
    def key_events(self):
        return pygame.event.get()

class State:
    background = None
    Spaceship = None
    def __init__(self):
        self.x = 1048//2-95
        self.y = 768//2+200
        self.background = Background.Background()
        self.Spaceship = Spaceship(pygame.image.load('ufo4.png'))

    def getSpaceship(self):
        return self.Spaceship;
    def update(self, d_t, dir): 
        self.x += dir.x*500*d_t # update circle position based on its velocity and d_t
        self.y += dir.y*500*d_t # update circle position based on its velocity and d_t
        self.getSpaceship().setPosiiton((self.x,self.y))
    def render(self, surface):  
        self.background.render(surface)
        # pygame.draw.circle(surface, (0,0,0), (self.x, self.y), 100, 10)
        self.Spaceship.render(surface)


def main():
    surface = create_main_surface()
    keyboard = Keyboard()
    player_controller = PlayerController(keyboard)
    state = State()
    running = True
    
    while (running == True):
        d_t = clock.tick()/1000 # update the clock and get time since the last call of .tick()

        for e in keyboard.key_events():
            if (e.type == pygame.QUIT):
                running = False

    
        #process_key_input(state, pygame.key.get_pressed())
        state.update(d_t, player_controller.get_arrow_key_dir())
        render_frame(surface, state)

main()