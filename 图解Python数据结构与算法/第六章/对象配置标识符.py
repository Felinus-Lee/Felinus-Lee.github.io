class Node:
    def __init__(self, node_id, name):
        self.node_id = node_id
        self.name = name

class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_node(self, node):
        if node.node_id not in self.adj_list:
            self.adj_list[node.node_id] = node

    def add_edge(self, node1_id, node2_id):
        if node1_id in self.adj_list and node2_id in self.adj_list:
            if 'neighbors' not in vars(self.adj_list[node1_id]):
                self.adj_list[node1_id].neighbors = []
            self.adj_list[node1_id].neighbors.append(node2_id)

    def get_neighbors(self, node_id):
        node = self.adj_list.get(node_id, None)
        return vars(node).get('neighbors', []) if node else []

# 创建图并添加节点和边
graph = Graph()
nodes = [Node(1, 'A'), Node(2, 'A'), Node(3, 'B'), Node(4, 'B'), Node(5, 'C')]
for node in nodes:
    graph.add_node(node)

edges = [(1, 2), (1, 5), (2, 3), (2, 4)]
for edge in edges:
    graph.add_edge(edge[0], edge[1])

# 打印邻接列表
for node_id, node in graph.adj_list.items():
    print(f"{node.name}{node_id} -> {graph.get_neighbors(node_id)}")
