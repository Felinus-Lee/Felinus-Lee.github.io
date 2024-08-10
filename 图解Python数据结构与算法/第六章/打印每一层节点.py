class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def level_order_traversal(root):
    if not root:
        return []
    
    result = []
    queue = [root]
    
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.pop(0)
            level.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)
    
    return result

# 创建树节点
root = TreeNode("User A")
root.left = TreeNode("Friend B", TreeNode("Friend D"), TreeNode("Friend E"))
root.right = TreeNode("Friend C", None, TreeNode("Friend F"))

# 层次遍历
print(level_order_traversal(root))  # 输出: [['User A'], ['Friend B', 'Friend C'], ['Friend D', 'Friend E', 'Friend F']]
