import pygame
class Background:
    image = None
    def __init__(self):
        self.image = self.create_image()


    def create_image(self):
        return pygame.image.load('pexels-valiphotos-589840.jpg')
    def render(self,surface):
        surface.blit(self.image,(0,0))