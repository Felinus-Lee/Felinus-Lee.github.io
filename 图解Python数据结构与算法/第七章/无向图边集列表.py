class GraphEdgeList:
    def __init__(self):
        self.edges = []
    
    def add_edge(self, u, v):
        self.edges.append((u, v))
    
    def display_edges(self):
        for edge in self.edges:
            print(edge)

# 示例使用
graph = GraphEdgeList()
graph.add_edge("A", "B")  # A-B
graph.add_edge("A", "C")  # A-C
graph.add_edge("B", "D")  # B-D
graph.add_edge("B", "E")  # B-E

graph.display_edges()
