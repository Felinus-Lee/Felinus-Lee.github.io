import numpy as np

class UndirectedWeightedGraphIncidenceMatrix:
    def __init__(self, num_vertices, num_edges):
        self.num_vertices = num_vertices
        self.num_edges = num_edges
        self.matrix = np.zeros((num_vertices, num_edges), dtype=int)

    def add_edge(self, edge_index, u, v, weight):
        self.matrix[u-1][edge_index] = weight  # 在无向图中，两个顶点都存储正的权重
        self.matrix[v-1][edge_index] = weight

    def display_matrix(self):
        print("Incidence Matrix:")
        print(self.matrix)

# 示例使用
num_vertices = 4  # 顶点数
num_edges = 3     # 边数

undirected_weighted_graph = UndirectedWeightedGraphIncidenceMatrix(num_vertices, num_edges)
undirected_weighted_graph.add_edge(0, 1, 2, 2)  # 边 1 连接顶点 1 和 2，权重为 2
undirected_weighted_graph.add_edge(1, 2, 3, 3)  # 边 2 连接顶点 2 和 3，权重为 3
undirected_weighted_graph.add_edge(2, 3, 4, 4)  # 边 3 连接顶点 3 和 4，权重为 4

undirected_weighted_graph.display_matrix()
