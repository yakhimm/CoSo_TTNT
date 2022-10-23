from doctest import OutputChecker
import pygame, sys
from algorithm import Algorithm
from maze import MAZE

# Màu sắc mặc định
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
SILVER = (192,192,192)
GRAY = (105,105,105)

# class để vẽ maze trên python
class Draw_MAZE:
    # Khởi tạo:
    #   maps    : Bản đồ mà ta sẽ dùng để thực hiện (chưa converse thành maze)
    #   output  : Là 1 str() path của file output (theo yêu cầu)
    def __init__(self, maps, output):
        # path folder lưu hình ảnh
        self.path_img = 'img/'
        self.fileOut = output

        # Số liệu của maze
        self.maps = maps
        self.maze = maps.converse_maze()
        self.start = maps.start
        self.goal = maps.goal
        self.col = maps.column
        self.row = maps.row
        
        # Số liệu của screen và pygame
        self.section = 35
        self.screen_size = self.screen_width, self.screen_height = self.col * self.section, self.row * self.section
        self.screen = pygame.display.set_mode(self.screen_size)       
        self.width_per_section = self.screen_width / self.col
        self.height_per_section = self.screen_height / self.row
        self.size_per_section = (self.width_per_section, self.height_per_section)

    # Vị trí của tường và vật cản trong screen
    def convert_path(self, paths, size):
        temp = []
        for path in paths:
            temp.append(((path[1] * size[0], path[0] * size[1]), size))
        return temp

    # Hàm để chạy 1 thuật toán search
    #   choice: lựa chọn thuật toán 
    def run(self, choice, heuristic = 1):
        conv_walls = self.convert_path(self.maps.walls, self.size_per_section)
        conv_barriers = self.convert_path(self.maps.barriers, self.size_per_section)
        
        # Hình ảnh trong pygame
        # Lựa chọn background
        bg_img = 0
        if self.screen_width < self.screen_height:
            bg_img = 1
        else: 
            bg_img = 2
        background = pygame.image.load(self.path_img + 'grass' + str(bg_img) + '.jpg')
        background = pygame.transform.scale(background, self.screen_size)

        # Hình cái cữa ~ Lối ra (EXIT)
        door = pygame.image.load(self.path_img + 'door.png')
        door = pygame.transform.scale(door, self.size_per_section)

        # Hình con chó ~ Bắt đầu (Start)
        dog = pygame.image.load(self.path_img + 'dog.jpg')
        dog = pygame.transform.scale(dog, self.size_per_section)

        # Hình bức tường ~ Biên của maze
        walls_img = pygame.image.load(self.path_img + 'block_stone.jpg')
        walls_img = pygame.transform.scale(walls_img, self.size_per_section)

        # Vật cãn, hòn đá ~ Vị trí không thể đi được trong maze 
        barriers_img = pygame.image.load(self.path_img + 'stone.png')
        barriers_img = pygame.transform.scale(barriers_img, self.size_per_section)

        # Vẽ các hình trên lên pygame
        self.screen.blit(background, (0, 0))
        for wall in conv_walls:
            self.screen.blit(walls_img, wall)
        for barrier in conv_barriers:
            self.screen.blit(barriers_img, barrier)
        self.screen.blit(dog, (self.start[1] * self.section, self.start[0] * self.section))
        pygame.draw.rect(self.screen, YELLOW, ((self.goal[1] * self.section,
                                                self.goal[0] * self.section), self.size_per_section))
        self.screen.blit(door, (self.goal[1] * self.section, self.goal[0] * self.section))

        # Tính toán thuật toán
        # pos là mảng vị trí đường đi
        pos = None
        algo = Algorithm(self.maps, self.screen, self.path_img, self.fileOut)
        # Lựa chọn tính toán 
        if (choice == 1):
            pos = algo.bfs()
        if (choice == 2):
            pos = algo.dfs()
        if (choice == 3):
            pos = algo.ucs()
        if (choice == 4):
            pos = algo.gbfs(heuristic)
        if (choice == 5):
            pos = algo.A_star(heuristic) 
        # Sau khi tính toán mà pos không có phần tử ~ pos = None thì viết ra output là NO 
        if pos == None:
            with open(self.fileOut +'.txt', 'w') as f:
                f.write('NO')
        # Update lại pygame
        pygame.display.update()      