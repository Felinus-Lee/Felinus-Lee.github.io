class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def is_complete_binary_tree(root):
    if not root:
        return True
    
    queue = [root]
    encountered_none = False
    
    while queue:
        node = queue.pop(0)
        if node:
            if encountered_none:
                return False
            queue.append(node.left)
            queue.append(node.right)
        else:
            encountered_none = True
    
    return True

# 构建树节点
root = TreeNode(1)
root.left = TreeNode(2, TreeNode(4), TreeNode(5))
root.right = TreeNode(3, None, TreeNode(6))

# 检查是否是完全二叉树
print(is_complete_binary_tree(root))  # 输出: True
