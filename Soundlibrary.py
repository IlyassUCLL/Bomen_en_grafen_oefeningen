import pygame
class SoundLibrary:
    explosion = False
    first = 0
    def __init__(self, file=str):
        if file == 'explosion':
            self.explosion = pygame.mixer.Sound('subdir/5.wav'
                                                )
    def uitvoering(self):
        pygame.init()
        var = pygame.mixer.Sound.play(self.explosion)
        while(var.get_busy()):
            pygame.time.wait(100)

