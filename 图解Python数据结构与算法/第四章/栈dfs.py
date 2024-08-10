def dfs_iterative(start):
    stack = [start]
    visited = set()
    
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            # 将邻居节点压入栈
            stack.extend(neighbor for neighbor in node.neighbors if neighbor not in visited)
