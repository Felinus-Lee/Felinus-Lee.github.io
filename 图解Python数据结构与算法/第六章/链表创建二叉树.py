# 定义节点类
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

# 打印二叉树
def print_tree(node, level=0, label="."):
    indent = "   " * level
    print(f"{indent}{label}: {node.value}")
    if node.left:
        print_tree(node.left, level + 1, "L")
    if node.right:
        print_tree(node.right, level + 1, "R")

print_tree(root)
