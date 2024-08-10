class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def preorder_traversal(root):
    result = []
    def traverse(node):
        if node:
            result.append(node.value)  # 访问根节点
            traverse(node.left)       # 前序遍历左子树
            traverse(node.right)      # 前序遍历右子树
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

# 前序遍历
print(preorder_traversal(root))  # 输出: [1, 2, 4, 5, 3, 6]
