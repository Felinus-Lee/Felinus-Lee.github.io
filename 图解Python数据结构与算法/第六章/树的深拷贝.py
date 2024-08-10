class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def clone_tree(root):
    if not root:
        return None
    new_root = TreeNode(root.value)
    new_root.left = clone_tree(root.left)
    new_root.right = clone_tree(root.right)
    return new_root

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

# 克隆树
cloned_root = clone_tree(root)
