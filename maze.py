from asyncio.windows_events import NULL

class MAZE:    
    # Cột và dòng của maze
    row = 0
    column = 0
    # Vị trí của maze trong file
    pos_maze = 0
    # maze ~ map
    maze = []
    # Số lượng điểm thưởng
    number_of_Rewards = 0
    rewards = []
    # Vị trí bắt đầu / kết thúc
    start = ()
    goal = ()

    def __init__(self, fileIn, fileOut):
    # File maps 'maps/bfs_map.txt'
        self.fileIn = fileIn
        self.fileOut = fileOut

    # Hàm mở file để vẽ maza
    def draw_maze(self):
        with open(self.fileOut, 'w') as outfile:
            outfile.write('0\n')
            outfile.write('xxxxxxxxxxxxxxxxxxxxxx\n')
            outfile.write('x   x   xx xx        x\n')
            outfile.write('x     x     xxxxxxxxxx\n')
            outfile.write('x x    xx  xxxx xxx xx\n')
            outfile.write('  x   x x xx   xxxx  x\n')
            outfile.write('x          xx  xx  x x\n')
            outfile.write('xxxxxxx x      xx  x x\n')
            outfile.write('xxxxxxxxx  x x  xx   x\n')
            outfile.write('x          x x Sx x  x\n')
            outfile.write('xxxxx x  x x x     x x\n')
            outfile.write('xxxxxxxxxxxxxxxxxxxxxx')

    # Hàm đọc vị trí của điểm thưởng (reward Point) và tìm kiếm đích (Goal) trong maze (Matrix)
    def read_maze(self):
        with open(self.fileIn, 'r') as f:
            rawMaze = f.read().split('\n')
            self.number_of_Rewards = int(rawMaze[0])
            self.pos_maze = self.number_of_Rewards + 1

            for i in range(1, self.pos_maze):
                reward = rawMaze[i].split(' ')
                self.rewards.append(reward[0], reward[1], reward[2])
                
            self.row = len(rawMaze) - self.pos_maze
            self.column = len(rawMaze[self.pos_maze])
            
            maze = []
            # Duyệt lại maze để xác định đích trong maze (Matrix)
            for i in range(self.pos_maze, len(rawMaze)):
                maze.append(rawMaze[i])
            # Kết quả trả về là 1 mê cung chưa qua chỉnh sữa
            return maze    

    def converse_maze(self):
        maze = self.read_maze()   
        for i in range(self.row):
            for j in range(self.column):
                if maze[i][j] == 'S':
                    self.start = (i, j)
                if (i == 0 or j == 0 or i == self.row - 1 or j == self.column - 1):
                    if (maze[i][j] == ' '):
                        maze[i] = maze[i].replace(" ", "G", 1)
                        self.goal = (i, j)
            self.maze.append(maze[i])

        return self.maze

fileIn = 'maps/bfs_map.txt'
fileOut = 'maps/bfs_map.txt'
maps = MAZE(fileIn, fileOut)
maze = maps.converse_maze()
print(maze)