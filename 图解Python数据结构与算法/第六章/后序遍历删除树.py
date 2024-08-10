class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def delete_tree(root):
    if not root:
        return
    
    delete_tree(root.left)  # 递归删除左子树
    delete_tree(root.right)  # 递归删除右子树
    print(f"Deleting node with value: {root.value}")
    del root

# 创建树节点
root = TreeNode(1)
root.left = TreeNode(2, TreeNode(4), TreeNode(5))
root.right = TreeNode(3, None, TreeNode(6))

# 删除树
delete_tree(root)
