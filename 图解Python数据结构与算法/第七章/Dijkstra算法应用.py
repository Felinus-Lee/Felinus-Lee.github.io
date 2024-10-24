import networkx as nx

# 创建一个有向加权图
G = nx.DiGraph()

# 添加边及其权重
G.add_weighted_edges_from([
    ('A', 'B', 3),
    ('A', 'C', 6),
    ('B', 'D', 2),
    ('B', 'C', 6),
    ('C', 'D', 4),
    ('D', 'E', 1)
])

# 计算从Start到Finish的最短路径
length, path = nx.single_source_dijkstra(G, 'A', target='E')

print("最短路径距离：", length)
print("最短路径：", path)
