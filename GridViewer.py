#
#   GridViewer.py
#
import maze
def View(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            
            if grid[i][j] == maze.EMPTY:
                print("  ", end = "")
                    
            elif grid[i][j] == maze.WALL:
                print("##", end = "")
                    
            elif grid[i][j] == maze.START:
                print("^^", end = "")
                    
            elif grid[i][j] == maze.END:
                print("$$", end = "")
                    
            elif grid[i][j] == maze.VISITED:
                print("..", end = "")
                    
            else:
                raise AssertionError
            
        print()
