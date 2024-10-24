from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(set)  # 使用 set 以避免重复边
        self.vertices = set()
    
    def add_vertex(self, v):
        self.vertices.add(v)
    
    def add_edge(self, u, v):
        self.graph[u].add(v)
        self.graph[v].add(u)  # 因为是无向图
    
    def induce_subgraph(self, vertex_set):
        subgraph = Graph()
        for v in vertex_set:
            subgraph.add_vertex(v)
        for u in vertex_set:
            for v in self.graph[u]:
                if v in vertex_set:
                    subgraph.add_edge(u, v)
        return subgraph

    def general_subgraph(self, vertex_set, edge_set):
        subgraph = Graph()
        for v in vertex_set:
            subgraph.add_vertex(v)
        for u, v in edge_set:
            subgraph.add_edge(u, v)
        return subgraph
    
    def display(self):
        for vertex in sorted(self.graph):
            print(f"{vertex} -> {sorted(self.graph[vertex])}")

# 使用示例
# 定义顶点集 V 和边集 E
V = {1, 2, 3, 4, 5}
E = {(1, 2), (1, 3), (2, 4), (3, 4), (4, 5)}

# 创建图实例
g = Graph()

# 添加顶点
for v in V:
    g.add_vertex(v)

# 添加边
for u, v in E:
    g.add_edge(u, v)

# 显示原图
print("原图:")
g.display()

# 生成诱导子图
induced_vertex_set = {1, 2, 4}
induced_subgraph = g.induce_subgraph(induced_vertex_set)
print("\n诱导子图:")
induced_subgraph.display()


# 生成一般子图
general_vertex_set = {1, 2, 3, 4}  # 选择顶点集合
general_edge_set = {(1, 2), (2, 3), (3, 4), (1, 4), (2, 4)}  # 增加的边
general_subgraph = g.general_subgraph(general_vertex_set, general_edge_set)
print("\n一般子图:")
general_subgraph.display()