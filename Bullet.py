import pygame
class bullet:
    position = None
    speed=750
    def __init__(self,position):
        self.position = position
    def render(self,surface):
        image = pygame.image.load("bullets/plasma.png")
        surface.blit(image,(500,500))
    def update(self,elapsed_seconds):
        x = self.position[0]
        y = self.position[1]
        y -= self.speed*elapsed_seconds
        self.position =(x,y)


