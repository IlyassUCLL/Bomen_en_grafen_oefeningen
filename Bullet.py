import pygame
class bullet:
    position = None
    speed=100
    def get_position(self):
        return self.position
    def __init__(self,position):
        self.position = position
    def render(self,surface):
        image = pygame.image.load("bullets/plasma.png")
        surface.blit(image,(self.position))
    def update(self,elapsed_seconds):
        x = self.position[0]
        y = self.position[1]
        y += self.speed*elapsed_seconds
        self.position = (x,y)


