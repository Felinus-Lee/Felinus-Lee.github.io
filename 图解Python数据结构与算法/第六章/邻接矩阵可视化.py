import matplotlib.pyplot as plt
import networkx as nx

class WeightedTree:
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        self.adj_matrix = [[0] * num_nodes for _ in range(num_nodes)]

    def add_edge(self, node1, node2, weight):
        if node1 >= 0 and node1 < self.num_nodes and node2 >= 0 and node2 < self.num_nodes:
            self.adj_matrix[node1][node2] = weight
            self.adj_matrix[node2][node1] = weight  # 对于无向图

    def display(self):
        for row in self.adj_matrix:
            print(row)

    def visualize(self):
        G = nx.Graph()

        # 添加节点
        for i in range(self.num_nodes):
            G.add_node(i)

        # 添加带权重的边
        for i in range(self.num_nodes):
            for j in range(i+1, self.num_nodes):  # 避免重复添加无向边
                if self.adj_matrix[i][j] != 0:
                    G.add_edge(i, j, weight=self.adj_matrix[i][j])

        pos = nx.spring_layout(G)  # 节点的布局

        # 绘制节点和边
        nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=700, font_size=16, font_weight='bold')
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=12)

        plt.show()

# 创建带权重的树并添加节点和边
tree = WeightedTree(5)
edges = [(0, 1, 2), (0, 2, 3), (1, 3, 4), (1, 4, 5)]
for edge in edges:
    tree.add_edge(edge[0], edge[1], edge[2])

# 打印带权重的邻接矩阵
tree.display()

# 可视化带权重的邻接矩阵
tree.visualize()
