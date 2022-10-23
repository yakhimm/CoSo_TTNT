from visualization import Draw_MAZE
from maze import MAZE
import pygame, sys
import time

if __name__ == '__main__':
    algo_search = { 1: 'bfs', 
                    2: 'dfs',
                    3: 'ucs',
                    4: 'gbfs',
                    5: 'astar' }

    pygame.init()
    running = True
    while (running):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        for i in range(1,6):
            maze = None
            input = 'input/level_1/input%d'%i + '.txt'
            for choice in algo_search.keys():    
                if choice == 4 or choice == 5:
                    for heur in range(1,3):
                        output = 'output/level_1/input%d'%i + '/' + algo_search[choice] + '/' + algo_search[choice] + '_heuristic_%d'%heur
                        pygame.display.set_caption(output + '.mp4')
                        maze = MAZE(input)
                        draw_maze = Draw_MAZE(maze, output)
                        draw_maze.run(choice, heur)
                else:
                    output = 'output/level_1/input%d'%i + '/' + algo_search[choice] + '/' + algo_search[choice]
                    pygame.display.set_caption(output + '.mp4')
                    maze = MAZE(input)
                    draw_maze = Draw_MAZE(maze, output)
                    draw_maze.run(choice)
                # Kết thúc vòng lặp
                if (choice == 5 and i == 5):
                    running = False
    time.sleep(3)
    pygame.quit()
    sys.exit()