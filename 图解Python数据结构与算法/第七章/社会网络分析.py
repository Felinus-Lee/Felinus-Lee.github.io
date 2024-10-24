import networkx as nx
import matplotlib.pyplot as plt

# 创建一个空的无向图
G = nx.Graph()

# 添加节点
G.add_node('Alice')
G.add_node('Bob')
G.add_node('Charlie')
G.add_node('Diana')

# 添加边（关系）
G.add_edge('Alice', 'Bob')
G.add_edge('Alice', 'Charlie')
G.add_edge('Bob', 'Charlie')
G.add_edge('Charlie', 'Diana')

# 打印基本信息
print("节点列表:", G.nodes())
print("边列表:", G.edges())
print("节点数量:", G.number_of_nodes())
print("边数量:", G.number_of_edges())

# 计算度中心性（每个节点的连接数）
degree_centrality = nx.degree_centrality(G)
print("度中心性:", degree_centrality)

# 绘制网络图
plt.figure(figsize=(8, 6))
pos = nx.spring_layout(G)  # 位置布局
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, edge_color='gray', font_size=15, font_weight='bold')
plt.title("社会网络图")
plt.show()
