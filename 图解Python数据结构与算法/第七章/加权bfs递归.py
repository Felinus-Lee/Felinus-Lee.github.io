def dfs_recursive(graph, node, visited=None):
    if visited is None:
        visited = set()
    
    visited.add(node)
    print(node, end=' ')
    
    for neighbor, _ in graph[node]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)
    
    return visited

graph = {
    'A': [('B', 4), ('C', 2), ('D', 5)],
    'B': [('A', 4), ('C', 1), ('E', 1)],
    'C': [('A', 2), ('B', 1), ('D', 3)],
    'D': [('A', 5), ('C', 3), ('E', 2)],
    'E': [('B', 1), ('D', 2)]
}

# 执行DFS递归
print("DFS Recursive Order:")
dfs_recursive(graph, 'A')
