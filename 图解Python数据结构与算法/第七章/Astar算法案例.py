import heapq

# 图结构：节点与相邻节点及其对应的边的权重
graph = {
    'A': [('B', 4), ('D', 2)],
    'B': [('C', 2), ('E', 5)],
    'C': [('F', 3)],
    'D': [('E', 1), ('G', 3)],
    'E': [('F', 2)],
    'F': [('G', 2)],
    'G': []
}

# 启发式函数h(n)的定义
h = {
    'A': 6,
    'B': 4,
    'C': 2,
    'D': 5,
    'E': 2,
    'F': 1,
    'G': 0
}

def a_star_search(graph, start, goal, h):
    open_list = []
    heapq.heappush(open_list, (0, start))
    came_from = {}
    g_score = {start: 0}  # 实际代价
    f_score = {start: h[start]}  # 总代价
    
    while open_list:
        current = heapq.heappop(open_list)[1]
        
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]
        
        for neighbor, cost in graph[current]:
            tentative_g_score = g_score[current] + cost
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + h[neighbor]
                heapq.heappush(open_list, (f_score[neighbor], neighbor))
    
    return None

start = 'A'
goal = 'G'
path = a_star_search(graph, start, goal, h)
print("最短路径：", path)
