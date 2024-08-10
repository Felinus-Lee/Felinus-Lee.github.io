class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# 创建节点
root = TreeNode('A')
root.left = TreeNode('B')
root.right = TreeNode('C')
root.left.left = TreeNode('D')
root.left.right = TreeNode('E')
root.right.right = TreeNode('F')

# 前序遍历函数
def preorder_traversal(node):
    if node:
        print(node.value, end=' ')
        preorder_traversal(node.left)
        preorder_traversal(node.right)

print("Preorder Traversal:")
preorder_traversal(root)
