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

def search(root, key):
    if root is None or root.val == key:
        return root
    
    if key < root.val:
        return search(root.left, key)
    else:
        return search(root.right, key)

def deleteNode(root, key):
    if root is None:
        return root

    if key < root.val:
        root.left = deleteNode(root.left, key)
    elif key > root.val:
        root.right = deleteNode(root.right, key)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        
        temp = minValueNode(root.right)
        root.val = temp.val
        root.right = deleteNode(root.right, temp.val)
    
    return root

def minValueNode(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

def print_tree(node, prefix="", is_left=True):
    if node is not None:
        print_tree(node.right, prefix + ("│   " if is_left else "    "), False)
        print(prefix + ("└── " if is_left else "┌── ") + str(node.val))
        print_tree(node.left, prefix + ("    " if is_left else "│   "), True)

# 示例操作
root = None
keys = [50, 30, 20, 40, 70, 60, 80]

# 插入操作
print("插入操作:")
for key in keys:
    root = insert(root, key)
    print(f"插入 {key} 后的树形：")
    print_tree(root)
    print("\n")

# 查找操作
print("查找操作:")
search_key = 40
result = search(root, search_key)
if result:
    print(f"找到节点：{search_key}")
else:
    print(f"未找到节点：{search_key}")
print_tree(root)
print("\n")

# 删除操作
print("删除操作:")
delete_key = 50
root = deleteNode(root, delete_key)
print(f"删除 {delete_key} 后的树形：")
print_tree(root)
print("\n")
