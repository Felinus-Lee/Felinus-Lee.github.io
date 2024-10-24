class DirectedGraphEdgeList:
    def __init__(self):
        self.edges = []
    
    def add_edge(self, u, v):
        self.edges.append((u, v))  # 记录边的方向
    
    def display_edges(self):
        for edge in self.edges:
            print(edge)

# 示例使用
graph = DirectedGraphEdgeList()
graph.add_edge("A", "B")  # A -> B
graph.add_edge("B", "C")  # B -> C
graph.add_edge("C", "D")  # C -> D
graph.add_edge("D", "A")  # D -> A

graph.display_edges()
