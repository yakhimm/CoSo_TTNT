import pygame, os 

# class để chụp hình ảnh của pygame
# có thể chụp nhiều ảnh -> tạo frame và xuất thành video
class Capture:
    def __init__(self, path):        
        split_path = path.split('/')
        self.name = split_path[len(split_path) - 1]
        self.path = path[:-len(self.name)]
        try: 
            os.makedirs(self.path)
        except OSError:
            pass

    def make_jpg(self, screen):
        fullpath = self.path + self.name + ".jpg"
        pygame.image.save(screen, fullpath)