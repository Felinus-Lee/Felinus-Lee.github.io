def bfs_with_all_paths(graph, start, end):
    queue = [(start, [start])]  # 初始时将起点及其路径放入队列中
    all_paths = []  # 用于存储所有找到的路径

    while queue:
        node, path = queue.pop(0)  # 出队
        if node == end:
            all_paths.append(path)  # 找到目标节点，将路径添加到结果列表中
        for neighbor in graph[node]:
            if neighbor not in path:  # 避免回路
                new_path = path + [neighbor]  # 生成新路径
                queue.append((neighbor, new_path))  # 将邻居节点及其路径加入队列
                # 输出搜索过程中的路径
                print("当前路径:", new_path)
    
    return all_paths

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

all_paths = bfs_with_all_paths(graph, start_node, end_node)
print("所有路径：", all_paths)
