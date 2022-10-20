
#from pickle import GLOBAL
#from tracemalloc import start
#from numpy import matrix


file_name = 'maze.txt'

'''------------------------------'''
class MAZE:
    #variables
    bonus = []           
    walls = []
    start = ()
    goal = ()
    matrix = []
    number_cols = 0
    number_rows = 0
    number_rewards = 0
    #########

    def __init__(self):
        self.set_value()

    def read_file(self,file_name: str = 'maze.txt'):
        f = open(file_name,'r')
        n_bonus_points = int(next(f)[:-1])
        #
        bonus_points = []
        #
        for i in range(n_bonus_points):
            x, y, reward = map(int, next(f)[:-1].split(' '))
            bonus_points.append((x, y, reward))

        text = f.read()

        matrix = [list(i) for i in text.splitlines()]

        f.close()
        
        #        
        
        return bonus_points, matrix

    def set_value(self):    #set variables of class
        self.bonus, self.matrix = self.read_file('maze.txt')

        self.number_rows = len(self.matrix)
        self.number_cols = len(self.matrix[0])
        for i in range(self.number_rows):
            for j in range(self.number_cols):
                if self.matrix[i][j] == "x":
                    self.walls.append((i,j))
                elif self.matrix[i][j] == "S":      #find start point
                    self.start = (i,j)
                    #find goal point
                if i == 0 and self.matrix[i][j] != "x":   
                    self.goal = (i,j)
                if j == 0 and self.matrix[i][j] != "x":
                    self.goal = (i,j)
                if i == self.number_rows - 1 and self.matrix[i][j] != "x":
                    self.goal = (i,j)