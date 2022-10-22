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
            for choice in algo_search.keys():
                input = 'input/level_1/input%d'%i + '.txt'
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