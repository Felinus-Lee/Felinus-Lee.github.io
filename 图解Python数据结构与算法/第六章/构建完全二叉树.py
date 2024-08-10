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

def build_complete_binary_tree(nodes):
    if not nodes:
        return None
    
    root = TreeNode(nodes[0])
    queue = [root]
    index = 1
    
    while index < len(nodes):
        node = queue.pop(0)
        if nodes[index] is not None:
            node.left = TreeNode(nodes[index])
            queue.append(node.left)
        index += 1
        
        if index < len(nodes) and nodes[index] is not None:
            node.right = TreeNode(nodes[index])
            queue.append(node.right)
        index += 1
    
    return root

# 构建完全二叉树
nodes = [1, 2, 3, 4, 5, None, 6]
complete_tree = build_complete_binary_tree(nodes)
print(level_order_traversal(complete_tree))  # 输出: [[1], [2, 3], [4, 5, 6]]
