class FrameBasedAnimation:
    images = None
    seconds = None
    def __init__(self, images=[],secondsPerFrame=int):
        time_passed = 0
        self.images = images
        self.seconds = secondsPerFrame
    def render(self,surface):


        if self.seconds == 0.05:
            surface.blit(self.images[1],(500,350))
        elif self.seconds == 0.1:
            surface.blit(self.images[2],(500,350))
        elif self.seconds == 0.2:
            surface.blit(self.images[3],(500,350))
        elif self.seconds == 0.3:
            surface.blit(self.images[4],(500,350))
        elif self.seconds == 0.4:
            surface.blit(self.images[5],(500,350))
        elif self.seconds == 0.5:
            surface.blit(self.images[6],(500,350))
        elif self.seconds == 0.6:
            surface.blit(self.images[7], (500, 350))
        elif self.seconds == 0.7:
            surface.blit(self.images[8],(500,350))
        elif self.seconds == 0.8:
            surface.blit(self.images[9],(500,350))
    def update(self,elapsedtime):
        self.seconds=elapsedtime





