class ChildSiblingTreeNode:
    def __init__(self, value):
        self.value = value
        self.first_child = None
        self.next_sibling = None

class ChildSiblingTree:
    def __init__(self):
        self.root = None

    def add_child(self, parent, child_value):
        child = ChildSiblingTreeNode(child_value)
        if parent.first_child is None:
            parent.first_child = child
        else:
            sibling = parent.first_child
            while sibling.next_sibling is not None:
                sibling = sibling.next_sibling
            sibling.next_sibling = child

    def set_root(self, root_value):
        self.root = ChildSiblingTreeNode(root_value)

    def traverse_preorder(self, node):
        if node is not None:
            print(node.value, end=' ')
            self.traverse_preorder(node.first_child)
            self.traverse_preorder(node.next_sibling)

# Example usage
tree = ChildSiblingTree()
root = ChildSiblingTreeNode(1)
tree.set_root(root.value)

# Adding children to the root
tree.add_child(root, 2)
tree.add_child(root, 3)
tree.add_child(root, 4)

# Adding children to node 2
node_2 = root.first_child  # node with value 2
tree.add_child(node_2, 5)
tree.add_child(node_2, 6)

# Adding child to node 3
node_3 = node_2.next_sibling  # node with value 3
tree.add_child(node_3, 7)

# Traverse the tree
print("Pre-order traversal:")
tree.traverse_preorder(root)
