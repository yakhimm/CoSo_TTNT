import pygame, os 

class Capture:
    def __init__(self, path):
        self.path = path
        
        try: 
            os.makedirs(self.path)
        except OSError:
            pass

    def make_png(self, screen):
        fullpath = self.path + ".jpg"
        pygame.image.save(screen, fullpath)