import numpy as np

class UndirectedGraphIncidenceMatrix:
    def __init__(self, num_vertices, num_edges):
        self.num_vertices = num_vertices
        self.num_edges = num_edges
        self.matrix = np.zeros((num_vertices, num_edges), dtype=int)

    def add_edge(self, edge_index, u, v):
        self.matrix[u-1][edge_index] = 1  # 顶点编号从1开始
        self.matrix[v-1][edge_index] = 1

    def display_matrix(self):
        print("Incidence Matrix:")
        print(self.matrix)

# 示例使用
num_vertices = 4  # 顶点数
num_edges = 3     # 边数

undirected_graph = UndirectedGraphIncidenceMatrix(num_vertices, num_edges)
undirected_graph.add_edge(0, 1, 2)  # 边 1 连接顶点 1 和 2
undirected_graph.add_edge(1, 2, 3)  # 边 2 连接顶点 2 和 3
undirected_graph.add_edge(2, 3, 4)  # 边 3 连接顶点 3 和 4

undirected_graph.display_matrix()
