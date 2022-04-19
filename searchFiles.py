import os
import os.path
import pygame
import random
import re
class searchPath:
    path=[]
    table=[]
    def __init__(self):
        pygame.init()
        self.path = self.determine_path("wav")
        self.table=self.create_sound_table(self.path)

    def find_audio_file(self, name=str):
        files=[]
        for dirpath, dirnames, filenames in os.walk("."):
            for filename in [f for f in filenames if f.endswith(".wav")]:
                if os.path.join(filename)[-3:] == name:
                    files.append( os.path.join(dirpath, filename))
        return files

    def derive_id(self,name=str):

        files =  self.find_audio_file(name)

        return files
    def determine_path(self, name=str):
        files = self.derive_id(name)
        for item in range(len(files)):
            files[item] = os.path.relpath(files[item])
            files[item] = files[item].replace("\\","/")
        return files



    def create_sound_table(self, arr=[]):

        table = []
        for item in arr:
            soundx = pygame.mixer.Sound(item)
            table.append(soundx)
        return table
    def play_random_explosion(self):
        x=random.randint(0,len(self.table)-1)
        self.table[x].play()
        while (pygame.mixer.get_busy()):
            pygame.time.wait(100)

pygame.init()
object = searchPath()
object.play_random_explosion()
