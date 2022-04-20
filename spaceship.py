class spaceship:
    image = None
    def __init__(self, image):
        self.image = image
    def render(self,surface):
        surface.blit(self.image,(0,0))