def dfs(node, visited):
    # 基本情况
    if node in visited:
        return
    visited.add(node)
    
    # 对每个邻居节点进行深度优先搜索
    for neighbor in node.neighbors:
        dfs(neighbor, visited)
