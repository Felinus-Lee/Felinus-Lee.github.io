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

# 创建带权重的树并添加节点和边
tree = WeightedTree(5)
edges = [(0, 1, 2), (0, 2, 3), (1, 3, 4), (1, 4, 5)]
for edge in edges:
    tree.add_edge(edge[0], edge[1], edge[2])

# 打印带权重的邻接矩阵
tree.display()
