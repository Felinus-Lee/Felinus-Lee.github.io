class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def inorder_traversal(root):
    result = []
    def traverse(node):
        if node:
            traverse(node.left)
            result.append(node.value)
            traverse(node.right)
    traverse(root)
    return result

# 示例树
#       1
#      / \
#     2   3
#    / \   \
#   4   5   6

# 创建树节点
root = TreeNode(1)
root.left = TreeNode(2, TreeNode(4), TreeNode(5))
root.right = TreeNode(3, None, TreeNode(6))

# 中序遍历
print(inorder_traversal(root))  # 输出: [4, 2, 5, 1, 3, 6]
