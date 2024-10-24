from collections import deque

def bfs(graph, start):
    visited = set()        # 初始化已访问节点集合
    queue = deque([start]) # 使用队列初始化，队列中只包含起始节点

    while queue:
        vertex = queue.popleft() # 从队列的左端取出一个节点
        if vertex not in visited:
            visited.add(vertex)  # 将节点标记为已访问
            print(vertex, end=' ') # 输出当前节点

            # 将当前节点的所有未访问邻居加入队列
            queue.extend(neighbor for neighbor, _ in graph[vertex] if neighbor not in visited)

    return visited

graph = {
    'A': [('B', 4), ('C', 2), ('D', 5)],
    'B': [('A', 4), ('C', 1), ('E', 1)],
    'C': [('A', 2), ('B', 1), ('D', 3)],
    'D': [('A', 5), ('C', 3), ('E', 2)],
    'E': [('B', 1), ('D', 2)]
}

# 执行BFS
print("BFS Order:")
bfs(graph, 'A')
