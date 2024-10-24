class Graph:
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        # 初始化邻接矩阵为全零矩阵
        self.adj_matrix = [[0 for _ in range(num_nodes)] for _ in range(num_nodes)]
    
    def add_edge(self, u, v):
        # 添加边 u-v
        self.adj_matrix[u][v] = 1
        self.adj_matrix[v][u] = 1  # 无向图是对称的
    
    def display_matrix(self):
        for row in self.adj_matrix:
            print(row)

# 示例使用
num_nodes = 4
g = Graph(num_nodes)
g.add_edge(0, 1)  # A-B
g.add_edge(0, 3)  # A-D
g.add_edge(1, 2)  # B-C

g.display_matrix()
