def turn_right(direction):
    return (direction + 1) % 4

def turn_left(direction):
    return (direction - 1) % 4

def move_forward(x, y, direction):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 右、下、左、上
    dx, dy = directions[direction]
    return x + dx, y + dy

def is_within_bounds(x, y, maze):
    return 0 <= x < len(maze) and 0 <= y < len(maze[0])

def right_hand_rule(maze, x, y, direction, path):
    if (x, y) == (5, 5):
        path.append((x, y))
        return True
    
    right_direction = turn_right(direction)
    next_x, next_y = move_forward(x, y, right_direction)
    
    if is_within_bounds(next_x, next_y, maze) and maze[next_x][next_y] == 0:
        path.append((x, y))
        if right_hand_rule(maze, next_x, next_y, right_direction, path):
            return True
        path.pop()
    
    next_x, next_y = move_forward(x, y, direction)
    if is_within_bounds(next_x, next_y, maze) and maze[next_x][next_y] == 0:
        path.append((x, y))
        if right_hand_rule(maze, next_x, next_y, direction, path):
            return True
        path.pop()
    
    left_direction = turn_left(direction)
    next_x, next_y = move_forward(x, y, left_direction)
    
    if is_within_bounds(next_x, next_y, maze) and maze[next_x][next_y] == 0:
        path.append((x, y))
        if right_hand_rule(maze, next_x, next_y, left_direction, path):
            return True
        path.pop()
    
    return False

def solve_maze_with_right_hand_rule(maze):
    start_x, start_y = 1, 1
    path = []
    initial_direction = 0  # 从右方向开始
    
    if right_hand_rule(maze, start_x, start_y, initial_direction, path):
        return path
    else:
        return "No path found"

maze = [
    [1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 0, 1, 1],
    [1, 0, 1, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 0, 1, 1, 1]
]

path = solve_maze_with_right_hand_rule(maze)
print("Path:", path)
