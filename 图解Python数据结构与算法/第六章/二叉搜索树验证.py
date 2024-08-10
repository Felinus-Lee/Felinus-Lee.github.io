class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def is_valid_bst(root):
    def inorder_traversal(node):
        if node is None:
            return []
        # 中序遍历：左子树 -> 根节点 -> 右子树
        return inorder_traversal(node.left) + [node.value] + inorder_traversal(node.right)

    inorder_result = inorder_traversal(root)
    # 检查中序遍历结果是否为严格递增序列
    return all(inorder_result[i] < inorder_result[i + 1] for i in range(len(inorder_result) - 1))

# 示例树
#       2
#      / \
#     1   3

# 创建树节点
root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)

# 检查树是否为二叉搜索树
print(is_valid_bst(root))  # 输出: True

# 非二叉搜索树示例
#       5
#      / \
#     1   4
#        / \
#       3   6

non_bst_root = TreeNode(5)
non_bst_root.left = TreeNode(1)
non_bst_root.right = TreeNode(4, TreeNode(3), TreeNode(6))

# 检查树是否为二叉搜索树
print(is_valid_bst(non_bst_root))  # 输出: False
