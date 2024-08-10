class BinaryTree:
    def __init__(self):
        self.adj_list = {}

    def add_node(self, node):
        if node not in self.adj_list:
            self.adj_list[node] = {'left': None, 'right': None}

    def add_edge(self, parent, left=None, right=None):
        if parent in self.adj_list:
            self.adj_list[parent]['left'] = left
            self.adj_list[parent]['right'] = right
            if left is not None:
                self.add_node(left)
            if right is not None:
                self.add_node(right)

    def get_children(self, node):
        return self.adj_list.get(node, {'left': None, 'right': None})

# 创建树并添加节点和边
tree = BinaryTree()
nodes = ['A', 'B', 'C', 'D', 'E', 'F']
for node in nodes:
    tree.add_node(node)

tree.add_edge('A', 'B', 'C')
tree.add_edge('B', 'D', 'E')
tree.add_edge('C', None, 'F')

# 打印扩展邻接列表
for node in tree.adj_list:
    children = tree.get_children(node)
    print(f"{node} -> left: {children['left']}, right: {children['right']}")
