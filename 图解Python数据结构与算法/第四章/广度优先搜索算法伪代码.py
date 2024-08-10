def bfs(graph, start, end):
    queue = deque()  # 创建一个双向队列作为队列
    visited = set()  # 创建一个集合用于记录已访问的节点
    parent = {}  # 创建一个字典用于记录每个节点的父节点

    queue.append(start)  # 将起始节点加入队列
    visited.add(start)  # 将起始节点标记为已访问

    while queue:
        current = queue.popleft()  # 从队列左侧取出一个节点作为当前节点
        if current == end:  # 如果当前节点是目标节点
            return construct_path(parent, start, end)  # 返回构建的路径
        for neighbor in graph[current]:  # 遍历当前节点的邻居节点
            if neighbor not in visited:  # 如果邻居节点未被访问过
                queue.append(neighbor)  # 将邻居节点加入队列
                visited.add(neighbor)  # 将邻居节点标记为已访问
                parent[neighbor] = current  # 记录邻居节点的父节点为当前节点