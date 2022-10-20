from asyncio.windows_events import NULL

class MAZE:    
    M_raw = NULL
    # Cột và dòng của maze
    row = 0
    column = 0

    # Vị trí của maze trong file
    p_map = 0

    # maze ~ map
    maze = []

    # Số lượng điểm thưởng
    rePoint = 0

    # Vị trí bắt đầu / kết thúc
    start = []
    goal = []

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
            # Maze có ký tự, chưa mã hóa về matrix
            self.M_raw = f.read().split('\n') 

            # Số lượng điểm thưởng
            self.rePoint = int(self.M_raw[0])

            # Cập nhật vị trí của maze
            self.p_map = self.rePoint + 1

            # Số cột và dòng của maze (Matrix)
            self.row = len(self.M_raw) - int(self.rePoint)
            self.column = len(self.M_raw[self.p_map])
                
            # Duyệt lại maze để xác định đích trong maze (Matrix)
            for i in range(self.p_map, self.row):
                for j in range(0, self.column):
                    # Tìm vị trí bắt đầu
                    if self.M_raw[i][j] == 'S':
                        self.start = [i - self.p_map, j]
                    # Duyệt biên của maze (Matrix)
                    # Vì đích (Goal) ~ Exit sẽ nằm ngoài biên của maze (Matrix)
                    # Nên vị trí ngoài biên nào xuất hiện ' ' thì đó sẽ là đích (Goal) của maze (Matrix) 
                    if (i == self.p_map or j == 0 or i == self.row - 1 or j == self.column- 1):
                        if (self.M_raw[i][j] == ' '):
                            # Tìm đích (Goal) cho maze (Matrix)
                            # Dùng hàm replace để thay thế ký tự ' ' trong maze (Matrix)
                            temp = self.M_raw[i].replace(" ", "G", j + 1)      
                            self.M_raw[i] = temp
                            # Tìm vị trí kết thúc
                            self.goal = [i - self.p_map, j]
                            
                self.maze.append(self.M_raw[i])
            # Kết quả trả về là 1 mê cung
            return self.maze         