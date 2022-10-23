import pygame, os 

class Capture:
    def __init__(self, path):        
        split_path = path.split('/')
        self.name = split_path[len(split_path) - 1]
        self.path = path[:-len(self.name)]
        try: 
            os.makedirs(self.path)
        except OSError:
            pass

    def make_png(self, screen):
        fullpath = self.path + self.name + ".jpg"
        pygame.image.save(screen, fullpath)