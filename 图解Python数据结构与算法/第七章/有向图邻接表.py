from collections import defaultdict

class DirectedGraph:
    def __init__(self):
        self.adj_list = defaultdict(list)
    
    def add_edge(self, u, v):
        # 添加有向边 u->v
        self.adj_list[u].append(v)
    
    def display_adj_list(self):
        for node in self.adj_list:
            print(f"{node}: {', '.join(map(str, self.adj_list[node]))}")

# 示例使用
g = DirectedGraph()
g.add_edge("A", "B")  # A->B
g.add_edge("B", "C")  # B->C
g.add_edge("C", "A")  # C->A

g.display_adj_list()
