from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.vertices = set()
    
    def add_vertex(self, v):
        self.vertices.add(v)
    
    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)  # 因为是无向图
    
    def dfs(self, v, visited):
        visited[v] = True
        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                self.dfs(neighbor, visited)
    
    def connected_components(self):
        visited = {v: False for v in self.vertices}
        components = []
        for vertex in self.vertices:
            if not visited[vertex]:
                component = []
                self.dfs_collect(vertex, visited, component)
                components.append(component)
        return components

    def dfs_collect(self, v, visited, component):
        visited[v] = True
        component.append(v)
        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                self.dfs_collect(neighbor, visited, component)

    def find_bridges(self):
        bridges = []
        visited = {v: False for v in self.vertices}
        disc = {v: float('inf') for v in self.vertices}
        low = {v: float('inf') for v in self.vertices}
        parent = {v: None for v in self.vertices}
        
        def bridge_util(v, time):
            visited[v] = True
            disc[v] = low[v] = time + 1
            
            for neighbor in self.graph[v]:
                if not visited[neighbor]:
                    parent[neighbor] = v
                    bridge_util(neighbor, time + 1)
                    
                    low[v] = min(low[v], low[neighbor])
                    
                    if low[neighbor] > disc[v]:
                        bridges.append((v, neighbor))
                elif neighbor != parent[v]:
                    low[v] = min(low[v], disc[neighbor])
        
        for vertex in self.vertices:
            if not visited[vertex]:
                bridge_util(vertex, 0)
        
        return bridges
    
    def is_connected(self):
        visited = {v: False for v in self.vertices}
        start_vertex = next(iter(self.vertices))  # Get an arbitrary starting point
        self.dfs(start_vertex, visited)
        return all(visited.values())
    
    def display(self):
        for vertex in self.graph:
            print(f"{vertex} -> {self.graph[vertex]}")

# 使用示例
# 定义顶点集 V 和边集 E
V = {15, 19, 20, 35}
E = {(15, 19), (15, 20), (20, 35)}

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

# 判断图是否连通
if g.is_connected():
    print("图是连通的")
else:
    print("图不是连通的")

# 查找连通分量
components = g.connected_components()
print(f"连通分量: {components}")

# 查找图中的桥
bridges = g.find_bridges()
print(f"图中的桥: {bridges}")
