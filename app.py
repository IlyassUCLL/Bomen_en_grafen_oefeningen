import pygame
from pygame.display import flip

import Background
from FrameBasedAnimation import FrameBasedAnimation
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

        # returns vector 0 length zero if no key presses or normalized direction
        if (v.length() == 0):
            return pygame.Vector2(0,0)
        return v.normalize()
    
def render_frame(surface, state, explosion, d_t):
    clear_surface(surface, BG_COLOR) # render the frame
    state.render(surface, explosion, d_t)
    image = pygame.image.load('ufo4.png')
    surface.blit(image,(state.x-30, state.y-30))
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
    def __init__(self):
        self.x = 0
        self.y = 0
        self.background = Background.Background()
        self.frames = [pygame.image.load(f'explosion/{i}.png') for i in range(1, 9 + 1)]

    def update(self, d_t, dir): 
        self.x += dir.x*500*d_t # update circle position based on its velocity and d_t
        self.y += dir.y*500*d_t # update circle position based on its velocity and d_t

    def render(self, surface, explosion, d_t):  
        self.background.render(surface)
        render_explosion_temp(explosion, surface, d_t)
        pygame.draw.circle(surface, (0,0,0), (self.x, self.y), 100, 10)

def render_explosion_temp(explosion, surface, d_t):
    explosion.render(surface)
    explosion.update(d_t)

def main():
    surface = create_main_surface()
    keyboard = Keyboard()
    player_controller = PlayerController(keyboard)
    state = State()
    
    explosion = FrameBasedAnimation(state.frames, 0)
    running = True
    
    while (running == True):
        d_t = clock.tick()/1000 # update the clock and get time since the last call of .tick()

        for e in keyboard.key_events():
            if (e.type == pygame.QUIT):
                running = False


        state.update(d_t, player_controller.get_arrow_key_dir())
        print(explosion.seconds)
        render_frame(surface, state, explosion, d_t)

main()