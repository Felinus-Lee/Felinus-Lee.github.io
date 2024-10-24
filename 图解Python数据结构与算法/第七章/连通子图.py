from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(set)
    
    def add_edge(self, u, v):
        self.graph[u].add(v)
        self.graph[v].add(u)  # 因为是无向图
    
    def find_connected_components(self):
        visited = set()
        components = []

        def bfs(start):
            queue = deque([start])
            component = set()
            while queue:
                vertex = queue.popleft()
                if vertex not in visited:
                    visited.add(vertex)
                    component.add(vertex)
                    queue.extend(self.graph[vertex] - visited)
            return component
        
        for vertex in self.graph:
            if vertex not in visited:
                component = bfs(vertex)
                components.append(component)
        
        return components

    def display(self):
        for vertex in sorted(self.graph):
            print(f"{vertex} -> {sorted(self.graph[vertex])}")

# 使用示例
# 创建图实例
g = Graph()

# 添加边
edges = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 1), (2, 6)]
for u, v in edges:
    g.add_edge(u, v)

# 显示图
print("原图:")
g.display()

# 查找连通分量
connected_components = g.find_connected_components()
print("\n连通子图:")
for component in connected_components:
    print(component)
