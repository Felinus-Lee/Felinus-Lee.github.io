from collections import deque

def bfs(maze, start, end):
    # 定义方向：上、下、左、右
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    rows, cols = len(maze), len(maze[0])
    
    # 记录访问过的位置
    visited = set()
    visited.add(start)
    
    # 使用队列来进行广度优先搜索
    queue = deque([(start, 0)])  # 元素为当前位置和步数
    
    while queue:
        (x, y), steps = queue.popleft()
        print("当前位置:", (x, y), "步数:", steps)
        
        if (x, y) == end:
            print("找到出口，步数:", steps)
            return
        
        # 探索当前位置的相邻位置
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == '0' and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append(((nx, ny), steps + 1))
    
    print("搜索结束，没有找到出口。")

maze = [
    "0011111111",
    "1000100011",
    "1110001111",
    "1000100011",
    "1111111000"
]

start = (0, 0)  # 起点坐标
end = (4, 9)    # 终点坐标

bfs(maze, start, end)
