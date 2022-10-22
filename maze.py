from asyncio.windows_events import NULL

class MAZE:    
    # Cột và dòng của maze
    row = 0
    column = 0
    # Vị trí của maze trong file
    pos_maze = 0
    
    # Số lượng điểm thưởng
    number_of_Rewards = 0
    rewards = []
    # Vị trí bắt đầu / kết thúc
    start = ()
    goal = ()  

    def __init__(self, fileIn):
    # File maps 'maps/bfs_map.txt'
        self.fileIn = fileIn

    # Hàm đọc vị trí của điểm thưởng (reward Point) và tìm kiếm đích (Goal) trong maze (Matrix)
    def read_maze(self):
        with open(self.fileIn, 'r') as f:
            split_maze = f.read().split('\n')
            self.number_of_Rewards = int(split_maze[0])
            self.pos_maze = self.number_of_Rewards + 1

            for i in range(1, self.pos_maze):
                reward = split_maze[i].split(' ')
                self.rewards.append(reward[0], reward[1], reward[2])
                
            self.row = len(split_maze) - self.pos_maze
            self.column = len(split_maze[self.pos_maze])
            
            raw_maze = []
            # Duyệt lại maze để xác định đích trong maze (Matrix)
            for i in range(self.pos_maze, len(split_maze)):
                raw_maze.append(split_maze[i])
            # Kết quả trả về là 1 mê cung chưa qua chỉnh sửa
            return raw_maze    

    def converse_maze(self):
        # maze ~ map
        self.walls = []
        self.barriers = []
        self.maze = []
        conv_maze = self.read_maze()
        for i in range(self.row):
            for j in range(self.column):   
                if conv_maze[i][j] == 'S':
                    self.start = (i, j)
                if (i == 0 or j == 0 or i == self.row - 1 or j == self.column - 1):
                    if (conv_maze[i][j] == ' '):
                        conv_maze[i] = conv_maze[i].replace(" ", "G", 1)
                        self.goal = (i, j)
                    if conv_maze[i][j] == 'x':
                        self.walls.append((i, j))
                else:
                    if conv_maze[i][j] == 'x':
                        self.barriers.append((i, j))
            self.maze.append(conv_maze[i])
        return self.maze