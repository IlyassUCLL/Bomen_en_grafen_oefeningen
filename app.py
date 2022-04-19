import pygame


# Initialize Pygame
pygame.init()

def create_main_surface():
    # Tuple representing width and height in pixels
    screen_size = (1024, 768)

    # Create window with given size
    pygame.display.set_mode(screen_size)
def main():
    create_main_surface()
    while (True):
        a=0

main()