def bfs_with_backtracking(graph, start, end):
    queue = [(start, [start])]  # 初始时将起点及其路径放入队列中

    while queue:
        node, path = queue.pop(0)  # 出队
        if node == end:
            return path  # 找到目标节点，直接返回路径
        for neighbor in graph[node]:
            if neighbor not in path:  # 避免回路
                new_path = path + [neighbor]  # 生成新路径
                queue.append((neighbor, new_path))  # 将邻居节点及其路径加入队列
                # 输出搜索过程中的路径
                print("当前路径:", new_path)

    return None  # 如果没找到路径，则返回 None

# 示例图结构
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

start_node = 'A'
end_node = 'F'

path = bfs_with_backtracking(graph, start_node, end_node)
print("回溯路径：", path)
