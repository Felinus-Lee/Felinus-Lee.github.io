class WeightedGraph:
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        # 初始化邻接矩阵为全零矩阵，表示无边的情况
        self.adj_matrix = [[0 for _ in range(num_nodes)] for _ in range(num_nodes)]
    
    def add_edge(self, u, v, weight):
        # 添加加权边 u-v
        self.adj_matrix[u][v] = weight
        self.adj_matrix[v][u] = weight  # 如果是无向加权图，加上这一行
    
    def display_matrix(self):
        for row in self.adj_matrix:
            print(row)

# 示例使用
num_nodes = 4
g = WeightedGraph(num_nodes)
g.add_edge(0, 1, 2)  # A-B，权重为2
g.add_edge(0, 3, 5)  # A-D，权重为5
g.add_edge(1, 2, 3)  # B-C，权重为3

g.display_matrix()
