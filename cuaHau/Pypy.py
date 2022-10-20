import os
import matplotlib.pyplot as plt


"""for mapId in range(1,6):
    bonus_points, matrix = read_file(f'Input/{mapId}.txt')
    print(f'The height of the matrix: {len(matrix)}')
    print(f'The width of the matrix: {len(matrix[0])}')

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j]=='S':
                start=(i,j)

            elif matrix[i][j]==' ':
                if (i==0) or (i==len(matrix)-1) or (j==0) or (j==len(matrix[0])-1):
                    end=(i,j)
                    
            else:
                pass
    path=[]
    visualize_maze(matrix,bonus_points,start,end,path)"""


from enum import Enum
from tkinter.ttk import *
from typing import NamedTuple
from tkinter import *
from typing import List
from search import goal_to_start,uniform
from search import goal_to_start
from maze import Maze
import visu

'''------------------------------------'''

# class for cell Position
class cell_positon(NamedTuple):  # namedtupes since use row and col as tuple
    r: int
    c: int

# cell class containg all the possiblities of a cell
class cell(str,Enum):
    path="*"
    staring_posi=""
    ending_posi=""
    obstracle="O"
    rewards = ""
    khali=" "

#class Grid
class grid:
    #default constructor:
    def __init__(self, maze, row: int = 10, col: int = 10,start:cell_positon=cell_positon(9,0), end:cell_positon=cell_positon(0,9)) ->None:
        self.row: int = row
        self.col: int = col
        self.start: cell_positon = start
        self.end: cell_positon = end
        self.maze = maze
        self.bonus = [] #[(point), val]
        # fill the grid empty cells
        self.g : List[List[cell]]  =   [[cell.khali for col in range(col)] for rows in range(row)] 
        
        
        # set obstacles
        self.set_obstacles()

        #setting start and ending position
        
        self.g[start.r][start.c]=cell.staring_posi
        self.g[end.r][end.c]=cell.ending_posi

    def set_obstacles(self):
        walls = self.maze.walls
        matrix = self.maze.matrix

        for point in walls:
            self.g[point[0]][point[1]] = cell.obstracle


    def check_end(self,c_p:cell_positon)-> bool:
        return c_p == self.end
         

    def check_next_node(self, c_p:cell_positon) -> List[cell_positon]:
        p: List[cell_positon]=[]
       
        if self.row > c_p.r + 1 and self.g[c_p.r +1][c_p.c] != cell.obstracle:
            p.append( cell_positon(c_p.r +1,c_p.c) )
        
      
        if  c_p.r - 1 >=0 and self.g[c_p.r -1][c_p.c] != cell.obstracle:
            p.append( cell_positon(c_p.r -1,c_p.c) )

       
        if  self.col > c_p.c + 1  and self.g[c_p.r][c_p.c+1] != cell.obstracle:
            p.append( cell_positon(c_p.r,c_p.c+1) )  

      
        if c_p.c -1 >= 0 and self.g[c_p.r][c_p.c - 1] != cell.obstracle:
            p.append(cell_positon( c_p.r,c_p.c-1) )   
       
        return p    
     # mark the path with "*""
    def mark_the_path(self, p:List[cell_positon]):
        total_cost = 0
        for c_p in p:
            self.g[c_p.r][c_p.c]=cell.path
            if self.g[c_p.r][c_p.c] == cell.rewards:
                for i in len(self.bonus):
                    if (self.bonus[0], self.bonus[1]) == self.g[c_p.r][c_p.c]:
                        total_cost+=self.bonus[2]
            total_cost+=1

        self.g[self.start.r][self.start.c]=cell.staring_posi
        self.g[self.end.r][self.end.c]=cell.ending_posi

        return total_cost


    def make_clear(self,p:List[cell_positon]):
        for items in p:
            self.g[items.r][items.c]=cell.khali

        self.g[self.start.r][self.start.c]=cell.staring_posi
        self.g[self.end.r][self.end.c]=cell.ending_posi

#########
def ucs():

    #Uniform cost Search
    print("----------------------------------------------")
    print("Path: Uniform cost Search \n")

    res_UCS= uniform(g.start,g.check_end,g.check_next_node)
    
    if res_UCS :
        way_UCS = goal_to_start(res_UCS)
        total_cost = g.mark_the_path(way_UCS)    
        #set the path    
        path_ucs=way_UCS 
        path_ucs.insert(0, g.start)
        #print(g)
        g.make_clear(way_UCS)  
        visu.visualize_maze(maze.matrix, maze.bonus, g.start, g.end, path_ucs)
    else:
        print("No uniform cost")
    
    print("ucs", total_cost)



maze = Maze()

rows = maze.number_rows
cols = maze.number_cols
s: cell_positon=cell_positon(maze.start[0], maze.start[1])
e: cell_positon=cell_positon(maze.goal[0], maze.goal[1])

g: grid = grid(maze, rows, cols, s, e)
ucs()
       
