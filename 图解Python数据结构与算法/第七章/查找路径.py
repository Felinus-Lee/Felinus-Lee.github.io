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
    
    def find_path(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if start not in self.graph:
            return None
        for node in self.graph[start]:
            if node not in path:
                newpath = self.find_path(node, end, path)
                if newpath:
                    return newpath
        return None

# 使用示例
# 定义顶点集 V 和边集 E
V = {15, 20, 35}
E = {(20, 15), (15, 35)}

# 创建图实例
g = UndirectedGraph()

# 添加顶点
for v in V:
    g.add_vertex(v)

# 添加边
for u, v in E:
    g.add_edge(u, v)

# 查找从顶点20到顶点35的路径
start, end = 20, 35
path = g.find_path(start, end)
if path:
    print(f"从顶点 {start} 到顶点 {end} 的路径是: {path}")
else:
    print(f"无法找到从顶点 {start} 到顶点 {end} 的路径")
