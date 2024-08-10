class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_node(self, node):
        if node not in self.adj_list:
            self.adj_list[node] = []

    def add_edge(self, node1, node2):
        if node1 in self.adj_list and node2 in self.adj_list:
            self.adj_list[node1].append(node2)
            # 如果是无向图，添加以下行
            # self.adj_list[node2].append(node1)

    def get_neighbors(self, node):
        return self.adj_list.get(node, [])

# 创建图并添加节点和边
graph = Graph()
nodes = [1, 2, 3, 4, 5]
for node in nodes:
    graph.add_node(node)

edges = [(1, 2), (1, 5), (2, 3), (2, 4)]
for edge in edges:
    graph.add_edge(edge[0], edge[1])

# 打印邻接列表
for node in graph.adj_list:
    print(f"{node} -> {graph.get_neighbors(node)}")
