class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def postorder_traversal(root):
    result = []
    
    def traverse(node):
        if not node:
            return
        traverse(node.left)  # 递归遍历左子树
        traverse(node.right)  # 递归遍历右子树
        result.append(node.value)  # 访问根节点
    
    traverse(root)
    return result

# 创建树节点
root = TreeNode(1)
root.left = TreeNode(2, TreeNode(4), TreeNode(5))
root.right = TreeNode(3, None, TreeNode(6))

# 后序遍历
print(postorder_traversal(root))  # 输出: [4, 5, 2, 6, 3, 1]
