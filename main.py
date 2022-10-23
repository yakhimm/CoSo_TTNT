from visualization import Draw_MAZE
from maze import MAZE
import pygame, sys
import time

if __name__ == '__main__':
    # Tạo 1 dictionary là các thuật toán tìm kiếm, được đánh số từ 1 đến 5
    algo_search = { 1: 'bfs', 
                    2: 'dfs',
                    3: 'ucs',
                    4: 'gbfs',
                    5: 'astar' }
    # Khởi chạy pygame (hoạt họa)
    pygame.init()
    running = True
    while (running):
        # Khi pygame đang load mà tắt thì sẽ dừng vòng lặp, tránh gây xung đột
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Vòng lặp test tất cả các input của chương trình
        for i in range(1,6):
            maze = None
            # input đi từ 1 -> 5
            input = 'input/level_1/input%d'%i + '.txt'
            for choice in algo_search.keys():   
                # Khi duyệt tới GBFS hoặc A* sẽ xét 2 heuristic sẵn có 
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

                # Kết thúc vòng lặp (Nếu thầy không muốn kết thúc nhanh thì xóa dòng này)
                if (choice == 5 and i == 5):
                    running = False
    # Dừng màn hình 3s rồi kết thúc chương trình
    time.sleep(3)
    pygame.quit()
    sys.exit()