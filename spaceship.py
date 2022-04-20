class Spaceship:
    image = None
    positition=(100,100)
    def __init__(self, image):
        self.image = image
    def render(self,surface):
        surface.blit(self.image,self.positition)