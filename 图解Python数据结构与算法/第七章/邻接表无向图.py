from collections import defaultdict

class Graph:
    def __init__(self):
        self.adj_list = defaultdict(list)
    
    def add_edge(self, u, v):
        # 添加边 u-v
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)  # 无向图中 v 也要连接 u
    
    def display_adj_list(self):
        for node in self.adj_list:
            print(f"{node}: {', '.join(map(str, self.adj_list[node]))}")

# 示例使用
g = Graph()
g.add_edge("A", "B")  # A-B
g.add_edge("A", "D")  # A-D
g.add_edge("B", "C")  # B-C

g.display_adj_list()
