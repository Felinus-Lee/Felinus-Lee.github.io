def bellman_ford(graph, start):
    # 初始化距离
    distance = {node: float('inf') for node in graph}
    distance[start] = 0

    # 对每条边进行 V-1 次松弛操作
    for _ in range(len(graph) - 1):
        for u in graph:
            for v, weight in graph[u]:
                if distance[u] + weight < distance[v]:
                    distance[v] = distance[u] + weight

    # 检测负权重环
    for u in graph:
        for v, weight in graph[u]:
            if distance[u] + weight < distance[v]:
                raise ValueError("Graph contains a negative-weight cycle")

    return distance

# 示例图
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', -2), ('D', 2)],
    'C': [('D', 3)],
    'D': []
}

# 运行 Bellman-Ford 算法
try:
    distances = bellman_ford(graph, 'A')
    print("Shortest distances from source 'A':")
    for node, dist in distances.items():
        print(f"Distance to {node}: {dist}")
except ValueError as e:
    print(e)
