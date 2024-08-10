class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def tree_height(root):
    if not root:
        return 0
    
    left_height = tree_height(root.left)  # 递归计算左子树高度
    right_height = tree_height(root.right)  # 递归计算右子树高度
    
    return max(left_height, right_height) + 1  # 当前节点高度为子树高度的最大值加1

# 创建树节点
root = TreeNode(1)
root.left = TreeNode(2, TreeNode(4), TreeNode(5))
root.right = TreeNode(3, None, TreeNode(6))

# 计算树高度
print(f"The height of the tree is: {tree_height(root)}")  # 输出: 3
