import pygame, sys
from collections import deque
from collections import Counter
import math
from priQueue import PriorityQueue
from capture import Capture

FPS = 10
fpsClock = pygame.time.Clock()
# class duyệt maza
class Algorithm:
    # Các tham số truyền vào là
    def __init__(self, maps, screen, path, fileOut):
        self.maze = maps.maze
        self.start = maps.start
        self.goal = maps.goal
        self.fileOut = fileOut
        # Tính dòng và cột 
        self.row = len(self.maze)
        self.col = len(self.maze[0])
        # Draw
        self.screen = screen
        self.path_img = path     
        self.capture = Capture(self.fileOut)
        self.size = (35, 35)
        self.flag_img = pygame.image.load(self.path_img + 'flag.png')
        self.flag_img = pygame.transform.scale(self.flag_img, self.size)

    # Chuyển đường đi từ str() thành [] chứa các vị trí pos
    def move2pos(self, path = ''):
        i = self.start[0]
        j = self.start[1]
        pos = []
        for move in path:
            if move == 'L':
                j -= 1
            elif move == 'R':
                j += 1
            elif move == 'U':
                i -= 1
            elif move == 'D':
                i += 1
            pos.append((i, j))
            if move != 'S':
                step = pygame.image.load(self.path_img + 'step' + move +'.png')
                step = pygame.transform.scale(step, self.size)
                self.update_pygame(step, (i, j), self.size)
        # Sau này sẽ in ra file txt
        with open(self.fileOut + '.txt', 'w') as f:
            f.write(str(len(path) - 1))
        return pos

    def update_pygame(self, img, pos, size):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        self.screen.blit(img, (pos[1] * size[0], pos[0] * size[1]))
        pygame.display.update()
        self.capture.make_png(self.screen)
        fpsClock.tick(FPS)

    def dfs(self):
        # Tập mở chứa các vị trí và đường đi (dùng stack)
        stack = deque()
        stack.append((self.start[0], self.start[1], 'S'))

        # way chỉ các bước Right - Lelf - Down - Up
        ways = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        # Các vị trí mà đã duyệt qua (lưu vết)
        visted = [[False] * self.col for _ in range(self.row)]

        flags = []
        while stack:
            # Xét vị trí tiếp theo
            curr = stack.pop()
            if (len(stack) != 0):
                flags.append((curr[0], curr[1]))
            # Khi đi qua thì duyệt True (đóng lại)
            visted[curr[0]][curr[1]] = True
            # Nếu gặp đích đến thì dừng
            if self.maze[curr[0]][curr[1]] == 'G':
                flags = Counter(flags)
                for flag in flags.keys():
                    self.update_pygame(self.flag_img, flag, self.size)
                # Khi gặp đích thì sẽ lưu vết dạng string (vd: SLLRLDULLLG) ~ S = start, G = goal
                pos = self.move2pos(curr[2])
                # Chuyển từ string về mảng chứa các vị trí
                return pos

            # Xét các neightbor của vị trí đó
            for way in ways:
                # neightbor_row = nr ~ neightbor_column = nc
                nr, nc = curr[0] + way[0], curr[1] + way[1]
                # Nếu ra ngoài maze hoặc vị trí đã close hoặc vị trí là 'x' thì không duyệt
                if (nr < 0 or nr >= self.row 
                    or nc < 0 or nc >= self.col 
                    or self.maze[nr][nc] == 'x' 
                    or visted[nr][nc]): continue
                # Mỡ đường đi
                if way == [0, 1]:
                    go = 'R'
                elif way == [0, -1]: 
                    go = 'L'
                elif way == [1, 0]:
                    go = 'D'
                elif way == [-1, 0]:
                    go = 'U'
                # Thêm đường đi vào tập mở, và chờ duyệt
                stack.append((nr, nc, curr[2] + go))  

    def bfs(self):
        # Tập mở chứa các vị trí và đường đi (dùng queue)
        queue = deque()
        queue.appendleft((self.start[0], self.start[1], 'S'))

        # way chỉ các bước Right - Lelf - Down - Up
        ways = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        # Các vị trí mà đã duyệt qua (lưu vết)
        visted = [[False] * self.col for _ in range(self.row)]
        flags = []
        while len(queue) != 0:
            # Đưa vào tập đóng
            close = queue.pop()
            if (len(queue) != 0):
                flags.append((close[0], close[1]))

            # Khi đi qua thì duyệt True (đóng lại)
            visted[close[0]][close[1]] = True
            # Nếu gặp đích đến thì dừng
            if self.maze[close[0]][close[1]] == 'G':
                flags = Counter(flags)
                for flag in flags.keys():
                    self.update_pygame(self.flag_img, flag, self.size)
                # Khi gặp đích thì sẽ lưu vết dạng string (vd: SLLRLDULLLG) ~ S = start, G = goal
                pos = self.move2pos(close[2])
                # Chuyển từ string về mảng chứa các vị trí
                return pos

            # Xét các neightbor của vị trí đó
            for way in ways:
                # neightbor_row = nr ~ neightbor_column = nc
                nr, nc = close[0] + way[0], close[1] + way[1]
                # Nếu ra ngoài maze hoặc vị trí đã close hoặc vị trí là 'x' thì không duyệt
                if (nr < 0 or nr >= self.row 
                    or nc < 0 or nc >= self.col 
                    or self.maze[nr][nc] == 'x' 
                    or visted[nr][nc]): continue

                # Mỡ đường đi
                if way == [0, 1]:
                    go = 'R'
                elif way == [0, -1]: 
                    go = 'L'
                elif way == [1, 0]:
                    go = 'D'
                elif way == [-1, 0]:
                    go = 'U'
                # Thêm đường đi vào tập mở, và chờ duyệt
                queue.appendleft((nr, nc, close[2] + go)) 
    
    def ucs(self):
        # Tập mở open dựa vào hàng đợi ưu tiên
        # Chứa vị trí i, j và đường đi 
        open = PriorityQueue()
        # Tạo vị trí bắt đầu
        # h(n) từ start->goal
        open.put(0, (self.start[0], self.start[1], 0, 'S'))

        # way chỉ các bước Right - Lelf - Down - Up
        ways = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        # Biến lưu vết các vị trí đã đi (close)
        visted = [[False] * self.col for _ in range(self.row)]  
        flags = []   
        while open.isEmpty() == False:
            # Lấy từ tập open -> tập close với node có chi phí tới goal bé nhất
            close = open.pop()
            if (open.isEmpty() == False):
                flags.append((close[1][0], close[1][1]))
            # close (lưu vết lại)
            visted[close[1][0]][close[1][1]] = True
            # Tương tự như bfs
            if self.maze[close[1][0]][close[1][1]] == 'G':
                flags = Counter(flags)
                for flag in flags.keys():
                    self.update_pygame(self.flag_img, flag, self.size)
                pos = self.move2pos(close[1][3])
                return pos
            for way in ways:
                # Tương tự: nr và nc là vị trí neightbor 
                nr, nc = close[1][0] + way[0], close[1][1] + way[1]
                # Nếu vượt phạm vi hoặc chạm 'x' hoặc đã đóng thì -> continue
                if (nr < 0 or nr >= self.row 
                    or nc < 0 or nc >= self.col 
                    or self.maze[nr][nc] == 'x' 
                    or visted[nr][nc]): continue  
                # Tính f_core ~ f(n')
                if way == [0, 1]:
                    go = 'R'
                elif way == [0, -1]: 
                    go = 'L'
                elif way == [1, 0]:
                    go = 'D'
                elif way == [-1, 0]:
                    go = 'U'
                
                cost = close[1][2] + 1
                if cost in open.keys():
                    while cost in open.keys():
                        cost = (cost + open.upper_keys(cost))/2 + 0.0000001
                # Đưa vào tập mở và chờ duyệt, với độ ưu tiên sẽ là f_core
                open.put(cost, (nr, nc, close[1][2] + 1, close[1][3] + go))

    # Heuristic tính khoản cách giữa vị trí pos đến đích
    def heuristic(self, pos, choice = 1):
        if choice == 1:
            return float(math.sqrt(pow(pos[0] - self.goal[0], 2) + pow(pos[1] - self.goal[1], 2)))
        else: 
            return abs(pos[0] - self.goal[0]) + abs(pos[1] - self.goal[1])
            
    def gbfs(self, choice = 1):
        # Tập mở open dựa vào hàng đợi ưu tiên
        # Chứa vị trí i, j và đường đi 
        open = PriorityQueue()
        # Tạo vị trí bắt đầu
        # h(n) từ start->goal
        curr_f = self.heuristic(self.start, choice)
        open.put(curr_f, (self.start[0], self.start[1], 'S'))

        # way chỉ các bước Right - Lelf - Down - Up
        ways = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        # Biến lưu vết các vị trí đã đi (close)
        visted = [[False] * self.col for _ in range(self.row)]
        flags = []
        while open.isEmpty() == False:
            # Lấy từ tập open -> tập close với node có chi phí tới goal bé nhất
            close = open.pop()
            if open.isEmpty() == False:
                flags.append((close[1][0], close[1][1]))
            # close (lưu vết lại)
            visted[close[1][0]][close[1][1]] = True
            # Tương tự như bfs
            if self.maze[close[1][0]][close[1][1]] == 'G':
                flags = Counter(flags)
                for flag in flags.keys():
                    self.update_pygame(self.flag_img, flag, self.size)
                pos = self.move2pos(close[1][2])
                return pos

            for way in ways:
                # Tương tự: nr và nc là vị trí neightbor 
                nr, nc = close[1][0] + way[0], close[1][1] + way[1]
                # Nếu vượt phạm vi hoặc chạm 'x' hoặc đã đóng thì -> continue
                if (nr < 0 or nr >= self.row 
                    or nc < 0 or nc >= self.col 
                    or self.maze[nr][nc] == 'x' 
                    or visted[nr][nc]): continue
                
                # Tính f_core ~ f(n')
                f_core = self.heuristic([nr, nc], choice)
                
                if f_core in open.keys():
                    while f_core in open.keys():
                        f_core = (f_core + open.upper_keys(f_core))/2 + 0.0000000001
                if way == [0, 1]:
                    go = 'R'
                elif way == [0, -1]: 
                    go = 'L'
                elif way == [1, 0]:
                    go = 'D'
                elif way == [-1, 0]:
                    go = 'U'
                # Đưa vào tập mở và chờ duyệt, với độ ưu tiên sẽ là f_core
                open.put(f_core, (nr, nc, close[1][2] + go))

    def A_star(self, choice = 1):
        # Tập mở open
        # Chứa vị trí i, j và g(n) và đường đi 
        open = PriorityQueue()
        # Tạo vị trí bắt đầu 
        curr_f = self.heuristic(self.start, choice)
        open.put(curr_f, (self.start[0], self.start[1], 0, 'S'))

        # way chỉ các bước Right - Lelf - Down - Up
        ways = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        # Biến lưu vết các vị trí đã đi (close)
        visted = [[False] * self.col for _ in range(self.row)]
        flags = []
        while open.isEmpty() == False:
            # Lấy từ tập open -> tập close
            close = open.pop()
            if open.isEmpty() == False:
                flags.append((close[1][0], close[1][1]))
            # close (lưu vết lại)
            visted[close[1][0]][close[1][1]] = True
            # Tương tự như bfs
            if self.maze[close[1][0]][close[1][1]] == 'G':
                flags = Counter(flags)
                for flag in flags.keys():
                    self.update_pygame(self.flag_img, flag, self.size)
                pos = self.move2pos(close[1][3])
                return pos

            for way in ways:
                # Tương tự: nr và nc là vị trí neightbor 
                nr, nc = close[1][0] + way[0], close[1][1] + way[1]
                # Nếu vượt phạm vi hoặc chạm 'x' hoặc đã đóng thì -> continue
                if (nr < 0 or nr >= self.row 
                    or nc < 0 or nc >= self.col 
                    or self.maze[nr][nc] == 'x' 
                    or visted[nr][nc]): continue
                
                # Tính f_core ~ f(n'), vì các bước đi tương tự nhau nên sẽ lấy close[2] ~ bước đi của cha + 1 -> g(n')
                h_core = self.heuristic([nr, nc])
                # f(n') = h(n') + g(n') 
                f_core = h_core + close[1][2] + 1 

                if way == [0, 1]:
                    go = 'R'
                elif way == [0, -1]: 
                    go = 'L'
                elif way == [1, 0]:
                    go = 'D'
                elif way == [-1, 0]:
                    go = 'U'

                if f_core in open.keys():
                    while f_core in open.keys():
                        f_core = (f_core + open.upper_keys(f_core))/2 + 0.0000000001
                # Đưa vào tập mở và chờ duyệt, với độ ưu tiên là f_core
                open.put(f_core, (nr, nc, close[1][2] + 1, close[1][3] + go))