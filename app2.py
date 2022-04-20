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
    
def render_frame(surface, state, d_t):
    clear_surface(surface, BG_COLOR) # render the frame
    state.render(surface, d_t)
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
        self.explosions = []

    def handle_event(self, event):
        if(event.type == pygame.MOUSEBUTTONDOWN):
            self.explosions.append(FrameBasedAnimation(self.frames, 0, (event.pos[0] - 25, event.pos[1]-31)))
            print("added explosion")

    def update(self, d_t, dir): 
        self.x += dir.x*500*d_t # update circle position based on its velocity and d_t
        self.y += dir.y*500*d_t # update circle position based on its velocity and d_t

        for exp in self.explosions:
            if (exp != None):
                exp.update(d_t)

    def render(self, surface, d_t):  
        self.background.render(surface)

        for i in range(0, len(self.explosions)):
            if (self.explosions[i] != None):
                if(self.explosions[i].seconds <= 0.8):
                    self.explosions[i].render(surface)
                else:
                    self.explosions[i] = None
                    print("removed explosion")

        pygame.draw.circle(surface, (0,0,0), (self.x, self.y), 100, 10)

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
            state.handle_event(e)



        state.update(d_t, player_controller.get_arrow_key_dir())
        render_frame(surface, state, d_t)

main()