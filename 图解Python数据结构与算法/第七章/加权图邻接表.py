from collections import defaultdict

class WeightedGraph:
    def __init__(self):
        self.adj_list = defaultdict(list)
    
    def add_edge(self, u, v, weight):
        # 添加加权边 u-v
        self.adj_list[u].append((v, weight))
        self.adj_list[v].append((u, weight))  # 无向加权图中 v 也要连接 u
    
    def display_adj_list(self):
        for node in self.adj_list:
            connections = ', '.join([f"({v}, {w})" for v, w in self.adj_list[node]])
            print(f"{node}: {connections}")

# 示例使用
g = WeightedGraph()
g.add_edge("A", "B", 2)  # A-B，权重为2
g.add_edge("A", "D", 5)  # A-D，权重为5
g.add_edge("B", "C", 3)  # B-C，权重为3

g.display_adj_list()
