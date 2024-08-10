class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def max_depth(root):
    if not root:
        return 0
    
    depth = 0
    queue = [root]
    
    while queue:
        depth += 1
        for _ in range(len(queue)):
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    
    return depth

# 创建树节点
root = TreeNode("Project Start")
root.left = TreeNode("Task A", TreeNode("Task C"), TreeNode("Task D"))
root.right = TreeNode("Task B", None, TreeNode("Task E"))

# 查找树的最大深度
print(max_depth(root))  # 输出: 3
