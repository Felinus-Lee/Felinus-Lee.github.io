from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.vertices = set()
    
    def add_vertex(self, v):
        self.vertices.add(v)
    
    def add_edge(self, u, v):
        if u not in self.vertices or v not in self.vertices:
            raise ValueError("Both vertices must be in the graph.")
        self.graph[u].append(v)
    
    def display(self):
        for vertex in self.graph:
            print(f"{vertex} -> {self.graph[vertex]}")

# 使用示例

# 定义顶点集 V 和边集 E
V = {1, 2, 3, 4}
E = {(1, 2), (1, 3), (2, 4)}

# 创建图实例
g = Graph()

# 添加顶点
for v in V:
    g.add_vertex(v)

# 添加边
for u, v in E:
    g.add_edge(u, v)

# 显示图
g.display()
