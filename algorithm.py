from collections import deque
from maze import MAZE
import math
from node import PriorityQueue

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
        # Sau này sẽ in ra file txt
        # for i, row in enumerate(self.maze):
        #     for j, col in enumerate(row):
        #         if (i, j) in pos:
        #             print('o', end ='')
        #         else:
        #             print(col, end = '')
        #     print()
        return pos

    def dfs(self):
        # Tập mở chứa các vị trí và đường đi (dùng stack)
        stack = deque()
        stack.append((self.start[0], self.start[1], 'S'))

        # way chỉ các bước Right - Lelf - Down - Up
        ways = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        # Các vị trí mà đã duyệt qua (lưu vết)
        visted = [[False] * self.col for _ in range(self.row)]

        while stack:
            # Xét vị trí tiếp theo
            curr = stack.pop()
            # Khi đi qua thì duyệt True (đóng lại)
            visted[curr[0]][curr[1]] = True
            # Nếu gặp đích đến thì dừng
            if self.maze[curr[0]][curr[1]] == 'G':
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

        while len(queue) != 0:
            # Đưa vào tập đóng
            close = queue.pop()
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
                queue.appendleft((nr, nc, close[2] + go))  

    # Heuristic tính khoản cách giữa vị trí pos đến đích
    def heuristic(self, pos):
        return math.sqrt(pow(pos[0] - self.goal[0], 2) + pow(pos[1] - self.goal[1], 2))
        # return abs(pos[0] - self.goal[0]) + abs(pos[1] - self.goal[1])
    def gbf(self):
        # Tập mở open dựa vào hàng đợi ưu tiên
        # Chứa vị trí i, j và đường đi 
        open = PriorityQueue()
        # Tạo vị trí bắt đầu
        # h(n) từ start->goal
        curr_f = self.heuristic(self.start)
        open.put(curr_f, (start[0], start[1], 'S'))

        # way chỉ các bước Right - Lelf - Down - Up
        ways = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        # Biến lưu vết các vị trí đã đi (close)
        visted = [[False] * self.col for _ in range(self.row)]
        while open.isEmpty() == False:
            # Lấy từ tập open -> tập close với node có chi phí tới goal bé nhất
            close = open.get()
            # close (lưu vết lại)
            visted[close[1][0]][close[1][1]] = True
            # Tương tự như bfs
            if self.maze[close[1][0]][close[1][1]] == 'G':
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
                f_core = self.heuristic([nr, nc])
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

    def A_star(self):
        # Tập mở open
        # Chứa vị trí i, j và g(n) và đường đi 
        open = PriorityQueue()
        # Tạo vị trí bắt đầu 
        curr_f = self.heuristic(self.start)
        open.put(curr_f, (start[0], start[1], 0, 'S'))

        # way chỉ các bước Right - Lelf - Down - Up
        ways = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        # Biến lưu vết các vị trí đã đi (close)
        visted = [[False] * self.col for _ in range(self.row)]
        while open.isEmpty() == False:
            # Lấy từ tập open -> tập close
            close = open.get()
            # close (lưu vết lại)
            visted[close[1][0]][close[1][1]] = True
            # Tương tự như bfs
            if self.maze[close[1][0]][close[1][1]] == 'G':
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
                # Đưa vào tập mở và chờ duyệt, với độ ưu tiên là f_core
                open.put(f_core, (nr, nc, close[1][2] + 1, close[1][3] + go))

# TEST
fileIn = 'maps/bfs_map.txt'
fileOut = 'maps/bfs_map.txt'
maps = MAZE(fileIn, fileOut)
maze = maps.read_maze()
start = maps.start
goal = maps.goal

algo = Algorithm(maze, start, goal)
aStar = algo.A_star()
gbf = algo.gbf()
bfs = algo.bfs()
dfs = algo.dfs()
print(bfs)
print(dfs)
print(aStar)
print(gbf)
