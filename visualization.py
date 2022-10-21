from ssl import AlertDescription
import pygame, sys
from maze import MAZE
from algorithm import Algorithm
from maze import MAZE
import time

FPS = 10
fpsClock = pygame.time.Clock()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
SILVER = (192,192,192)
GRAY = (105,105,105)

class Draw_MAZE:
    def __init__(self, maps):
        # path folder lưu hình ảnh
        self.path_img = 'C:/Users/ASUS/Desktop/CoSo_TTNT-master/Source/img/'

        # Số liệu của maze
        maze = maps.converse_maze()
        self.start = maps.start
        self.goal = maps.goal
        self.col = maps.column
        self.row = maps.row

        self.barriers = maps.barriers
        self.walls = maps.walls
        
        # Số liệu của screen
        self.section = 35
        self.screen_size = self.screen_width, self.screen_height = self.col * self.section, self.row * self.section
        self.screen = pygame.display.set_mode(self.screen_size)       
    
        # Tạo pygame
        self.width_per_section = self.screen_width / self.col
        self.height_per_section = self.screen_height / self.row
        self.size_per_section = (self.width_per_section, self.height_per_section)

        self.algo = Algorithm(maze, self.start, self.goal, self.screen, self.path_img)

    # Vị trí của tường và vật cản 
    def convert_path(self, paths, size):
        temp = []
        for path in paths:
            temp.append(((path[1] * size[0], path[0] * size[1]), size))
        return temp

    def run(self, choice):
        pygame.init()
        pygame.display.set_caption('MAZE')

        self.walls = self.convert_path(self.walls, self.size_per_section)
        self.barriers = self.convert_path(self.barriers, self.size_per_section)

        # Hình ảnh trong pygame
        bg_img = 0
        if self.screen_width < self.screen_height:
            bg_img = 1
        else: 
            bg_img = 2
        background = pygame.image.load(self.path_img + 'grass' + str(bg_img) + '.jpg')
        background = pygame.transform.scale(background, self.screen_size)

        door = pygame.image.load(self.path_img + 'door.png')
        door = pygame.transform.scale(door, self.size_per_section)

        dog = pygame.image.load(self.path_img + 'dog.jpg')
        dog = pygame.transform.scale(dog, self.size_per_section)

        walls_img = pygame.image.load(self.path_img + 'block_stone.jpg')
        walls_img = pygame.transform.scale(walls_img, self.size_per_section)

        barriers_img = pygame.image.load(self.path_img + 'stone.png')
        barriers_img = pygame.transform.scale(barriers_img, self.size_per_section)

        self.screen.blit(background, (0, 0))
        for wall in self.walls:
            self.screen.blit(walls_img, wall)
            # pygame.draw.rect(screen, GRAY, wall)
        for barrier in self.barriers:
            self.screen.blit(barriers_img, barrier)

        self.screen.blit(dog, (self.start[1] * self.section, self.start[0] * self.section))

        pygame.draw.rect(self.screen, YELLOW, ((self.goal[1] * self.section,
                                                self.goal[0] * self.section), self.size_per_section))
        self.screen.blit(door, (self.goal[1] * self.section, self.goal[0] * self.section))

        if (choice == 0):
            self.algo.bfs()
        if (choice == 1):
            self.algo.dfs()
        if (choice == 2):
            self.algo.ucs()
        if (choice == 3):
            self.algo.gbfs()
        if (choice == 5):
            self.algo.A_star()

        time.sleep(3)
        pygame.quit()
        sys.exit()

# TEST
fileIn = 'cuaHau/1.txt'
fileOut = 'maps/bfs_map.txt'
maps = MAZE(fileIn, fileOut)

draw = Draw_MAZE(maps)

# Choice theo thứ tự: BFS, DFS, UCS, GBFS, A*
choice = 0
draw.run(choice)