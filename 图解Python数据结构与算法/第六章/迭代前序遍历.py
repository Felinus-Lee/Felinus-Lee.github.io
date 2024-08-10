class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def preorder_traversal_iterative(root):
    if not root:
        return []
    result, stack = [], [root]
    while stack:
        node = stack.pop()
        if node:
            result.append(node.value)  # 访问根节点
            if node.right:
                stack.append(node.right)  # 将右子节点压入栈
            if node.left:
                stack.append(node.left)   # 将左子节点压入栈
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
print(preorder_traversal_iterative(root))  # 输出: [1, 2, 4, 5, 3, 6]
