from collections import deque
from main import MAZE
import math

# class duyệt maza
class Algorithm:
    # Các tham số truyền vào là maze, start, goal
    def __init__(self, maze, start, goal):
        self.maze = maze
        self.start = start
        self.goal = goal
        # Tính dòng và cột 
        self.row = len(maze)
        self.col = len(maze[0])

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
        # for i, row in enumerate(self.maze):
        #     for j, col in enumerate(row):
        #         if (i, j) in pos:
        #             print('o', end ='')
        #         else:
        #             print(col, end = '')
        #     print()
        return pos

    def bfs(self):
        # Tập mở chứa các vị trí và đường đi (dùng queue)
        open = deque()
        open.appendleft((self.start[0], self.start[1], 'S'))

        # way chỉ các bước Right - Lelf - Down - Up
        ways = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        # Các vị trí mà đã duyệt qua (lưu vết)
        visted = [[False] * self.col for _ in range(self.row)]

        while len(open) != 0:
            # Đưa vào tập đóng
            close = open.pop()
            # Khi đi qua thì duyệt True (đóng lại)
            visted[close[0]][close[1]] = True
            # Nếu gặp đích đến thì dừng
            if self.maze[close[0]][close[1]] == 'G':
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
                open.appendleft((nr, nc, close[2] + go))  

    # Heuristic tính khoản cách giữa vị trí pos đến đích
    def h_core(self, pos):
        return math.sqrt(pow(pos[0] - self.goal[0], 2) + pow(pos[1] - self.goal[1], 2))
        #return abs(pos[0] - self.goal[0]) + abs(pos[1] - self.goal[1])

    def A_star(self):
        # Tập mở open
        # Chứa vị trí i, j và g(n) và đường đi 
        open = deque()
        # Tạo vị trí bắt đầu
        open.appendleft((start[0], start[1], 0, 'S'))

        # way chỉ các bước Right - Lelf - Down - Up
        ways = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        # Biến lưu vết các vị trí đã đi (close)
        visted = [[False] * self.col for _ in range(self.row)]

        while len(open) != 0:
            # Lấy từ tập open -> tập close
            close = open.pop()
            # close (lưu vết lại)
            visted[close[0]][close[1]] = True
            # Tương tự như bfs
            if self.maze[close[0]][close[1]] == 'G':
                pos = self.move2pos(close[3])
                return pos

            # current_f(n) sẽ là hàm f(n)
            curr_f = self.h_core([close[0], close[1]]) + close[2]

            for way in ways:
                # Tương tự: nr và nc là vị trí neightbor 
                nr, nc = close[0] + way[0], close[1] + way[1]
                # Nếu vượt phạm vi hoặc chạm 'x' hoặc đã đóng thì -> continue
                if (nr < 0 or nr >= self.row 
                    or nc < 0 or nc >= self.col 
                    or self.maze[nr][nc] == 'x' 
                    or visted[nr][nc]): continue
                
                # Tính f_core ~ f(n'), vì các bước đi tương tự nhau nên sẽ lấy close[2] ~ bước đi của cha + 1 -> g(n')
                f_core = self.h_core([nr, nc]) + close[2] + 1
                # Nếu curr_f <= f_core thì sẽ duyệt (định hướng)
                if curr_f <= f_core:
                    if way == [0, 1]:
                        go = 'R'
                    elif way == [0, -1]: 
                        go = 'L'
                    elif way == [1, 0]:
                        go = 'D'
                    elif way == [-1, 0]:
                        go = 'U'
                    # Đưa vào tập mở và chờ duyệt
                    open.appendleft((nr, nc, close[2] + 1, close[3] + go))

# TEST
file = 'maps/bfs_map.txt'
maps = MAZE(file)
maze = maps.read_maze()
start = maps.start
goal = maps.goal

algo = Algorithm(maze, start, goal)
aStar = algo.A_star()
print(aStar)
bfs = algo.bfs()
print(bfs)