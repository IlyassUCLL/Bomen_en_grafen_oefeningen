class Spaceship:
    image = None
    positition=None
    def setPosiiton(self, position):
        self.positition = position;
    def getPosition(self):
        return self.positition
    def __init__(self, image):
        self.image = image
    def render(self,surface):
        surface.blit(self.image,self.positition)
