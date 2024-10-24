def dfs_iterative(graph, start):
    # 创建访问标记数组
    visited = [False] * len(graph)
    
    # 初始化栈并将起始节点压入栈中
    stack = [start]
    
    # 遍历栈
    while stack:
        # 弹出栈顶节点
        node = stack.pop()
        
        # 如果节点未被访问，则访问它
        if not visited[node]:
            print(node, end=' ')  # 访问节点
            visited[node] = True
            
            # 将当前节点的未访问邻居压入栈中
            for neighbor in reversed(graph[node]):
                if not visited[neighbor]:
                    stack.append(neighbor)

# 示例图的邻接表表示
graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 4],
    3: [1],
    4: [1, 2]
}

# 使用相同的邻接表表示
dfs_iterative(graph, 0)
