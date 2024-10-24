def is_valid_move(maze, x, y, visited):
    return (0 <= x < len(maze) and
            0 <= y < len(maze[0]) and
            maze[x][y] == 0 and
            not visited[x][y])

def solve_maze_recursive(maze, x, y, path, visited):
    if (x, y) == (len(maze) - 1, len(maze[0]) - 1):
        path.append((x, y))
        return True
    
    if is_valid_move(maze, x, y, visited):
        visited[x][y] = True
        path.append((x, y))
        
        if (solve_maze_recursive(maze, x + 1, y, path, visited) or
            solve_maze_recursive(maze, x, y + 1, path, visited) or
            solve_maze_recursive(maze, x - 1, y, path, visited) or
            solve_maze_recursive(maze, x, y - 1, path, visited)):
            return True
        
        path.pop()
        return False

    return False

def find_path_recursive(maze):
    path = []
    visited = [[False] * len(maze[0]) for _ in range(len(maze))]
    if solve_maze_recursive(maze, 0, 0, path, visited):
        return path
    else:
        return None
    
# 迷宫定义
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0]
]

# 使用示例
path_recursive = find_path_recursive(maze)
print("Recursive path:", path_recursive)