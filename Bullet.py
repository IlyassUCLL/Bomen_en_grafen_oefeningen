import pygame
class bullet:
    position = None
    def __init__(self,position):
        self.position = position
    def render(self,surface):
        image = pygame.image.load("bullets/plasma.png")
        surface.blit(image,(500,500))
    

