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
    
    def has_cycle_util(self, v, visited, parent):
        visited[v] = True
        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                if self.has_cycle_util(neighbor, visited, v):
                    return True
            elif parent != neighbor:
                return True
        return False
    
    def has_cycle(self):
        visited = {v: False for v in self.vertices}
        for vertex in self.vertices:
            if not visited[vertex]:
                if self.has_cycle_util(vertex, visited, -1):
                    return True
        return False

    def display(self):
        for vertex in self.graph:
            print(f"{vertex} -> {self.graph[vertex]}")

# 使用示例
# 定义顶点集 V 和边集 E
V = {15, 20, 35}
E = {(20, 15), (20, 35),(15,35)}

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

# 判断图中是否存在环
if g.has_cycle():
    print("图中存在环")
else:
    print("图中不存在环")
