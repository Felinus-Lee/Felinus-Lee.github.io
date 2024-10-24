import heapq

def dijkstra(graph, start):
    # 初始化距离表，将所有节点的距离设置为无穷大，起点的距离设置为0
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0

    # 优先队列，存储（当前距离，节点）
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # 如果当前节点的距离已经大于已知的最短距离，跳过
        if current_distance > distances[current_node]:
            continue
        
        # 更新相邻节点的距离
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            # 如果发现更短的路径，更新相邻节点的距离
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances

graph = {
    'A': {'B': 2, 'C': 1},
    'B': {'C': 3, 'D': 1},
    'C': {'D': 1},
    'D': {}
}


# 从节点A到所有节点的最短路径
shortest_paths = dijkstra(graph, 'A')
print(shortest_paths)
