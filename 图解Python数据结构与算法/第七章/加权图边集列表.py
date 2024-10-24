class WeightedGraphEdgeList:
    def __init__(self):
        self.edges = []  # 存储边的列表
    
    def add_edge(self, u, v, weight):
        """添加一条带权重的边"""
        self.edges.append((u, v, weight))
    
    def display_edges(self):
        """显示所有边及其权重"""
        for edge in self.edges:
            print(f"Edge from {edge[0]} to {edge[1]} with weight {edge[2]}")

# 示例使用
graph = WeightedGraphEdgeList()
graph.add_edge("A", "B", 2)  # 添加 A-B 边，权重为 2
graph.add_edge("B", "C", 3)  # 添加 B-C 边，权重为 3
graph.add_edge("C", "D", 4)  # 添加 C-D 边，权重为 4

graph.display_edges()
