from collections import defaultdict

class UndirectedGraph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.vertices = set()
    
    def add_vertex(self, v):
        self.vertices.add(v)
    
    def add_edge(self, u, v):
        if u not in self.vertices or v not in self.vertices:
            raise ValueError("Both vertices must be in the graph.")
        self.graph[u].append(v)
        self.graph[v].append(u)  # 因为是无向图
    
    def degree(self, v):
        return len(self.graph[v])
    
    def display(self):
        for vertex in self.graph:
            print(f"{vertex} -> {self.graph[vertex]}")

# 使用示例
# 定义顶点集 V 和边集 E
V = {6, 8, 15, 20, 35}
E = {(20, 15), (20, 6), (20, 8), (15, 35)}

# 创建图实例
g = UndirectedGraph()

# 添加顶点
for v in V:
    g.add_vertex(v)

# 添加边
for u, v in E:
    g.add_edge(u, v)

# 显示图
g.display()

# 计算顶点度
for v in V:
    print(f"顶点 {v} 的度是: {g.degree(v)}")
