class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return TreeNode(key)
    
    if key < root.val:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    
    return root

def generate_bst():
    root = None
    keys = [50, 30, 20, 40, 70, 60, 80]
    
    for key in keys:
        root = insert(root, key)
    
    return root

def inorder_traversal(root):
    if root is not None:
        inorder_traversal(root.left)
        print(root.val, end=' ')
        inorder_traversal(root.right)

bst_root = generate_bst()
print("Inorder traversal of the BST:")
inorder_traversal(bst_root)
