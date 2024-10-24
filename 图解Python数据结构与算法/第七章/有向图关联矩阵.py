import numpy as np

class DirectedGraphIncidenceMatrix:
    def __init__(self, num_vertices, num_edges):
        self.num_vertices = num_vertices
        self.num_edges = num_edges
        self.matrix = np.zeros((num_vertices, num_edges), dtype=int)

    def add_edge(self, edge_index, u, v):
        self.matrix[u-1][edge_index] = -1  # 边从 u 指向 v
        self.matrix[v-1][edge_index] = 1   # 边指向 v

    def display_matrix(self):
        print("Incidence Matrix:")
        print(self.matrix)

# 示例使用
num_vertices = 4  # 顶点数
num_edges = 3     # 边数

directed_graph = DirectedGraphIncidenceMatrix(num_vertices, num_edges)
directed_graph.add_edge(0, 1, 2)  # 边 1 从顶点 1 指向 2
directed_graph.add_edge(1, 2, 3)  # 边 2 从顶点 2 指向 3
directed_graph.add_edge(2, 3, 4)  # 边 3 从顶点 3 指向 4

directed_graph.display_matrix()
