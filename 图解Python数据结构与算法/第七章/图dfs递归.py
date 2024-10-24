def dfs(graph, node, visited):
    visited[node] = True
    print(node, end=' ')  # 访问节点
    
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited)

# 示例图的邻接表表示
graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 4],
    3: [1],
    4: [1, 2]
}

visited = [False] * len(graph)
dfs(graph, 0, visited)
