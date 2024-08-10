def build_adjacency_list(arr):
    adjacency_list = {}
    
    for i, node_value in enumerate(arr):
        neighbors = []
        
        # 计算相邻节点的索引
        left_index = i * 2 + 1
        right_index = i * 2 + 2
        
        # 添加相邻节点到列表
        if left_index < len(arr):
            neighbors.append(arr[left_index])
        if right_index < len(arr):
            neighbors.append(arr[right_index])
        
        # 将节点值及其相邻节点列表添加到邻接表中
        adjacency_list[node_value] = neighbors if neighbors else '[ ]'
    
    return adjacency_list

# 数组
arr = [2, 6, 8, 5, 3, 7, 1, 4]

# 构建邻接表
adj_list = build_adjacency_list(arr)

# 打印邻接表
for node_value, neighbors in adj_list.items():
    print(f"{node_value}: {neighbors}")
