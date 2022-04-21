import pygame
class bullet:
    def __init__(self):
        pass
    def render(self,surface):
        image = pygame.image.load("bullets/plasma.png")
        surface.blit(image,(500,500))

