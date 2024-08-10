class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def right_rotate(y):
    x = y.left
    T2 = x.right

    x.right = y
    y.left = T2

    return x

def left_rotate(x):
    y = x.right
    T2 = y.left

    y.left = x
    x.right = T2

    return y

def left_right_rotate(z):
    z.left = left_rotate(z.left)
    return right_rotate(z)

def right_left_rotate(z):
    z.right = right_rotate(z.right)
    return left_rotate(z)

def print_tree(node, level=0, prefix="Root: "):
    if node is not None:
        print(" " * (level * 4) + prefix + str(node.val))
        if node.left is not None or node.right is not None:
            if node.left:
                print_tree(node.left, level + 1, "L--- ")
            else:
                print(" " * ((level + 1) * 4) + "L--- None")
            if node.right:
                print_tree(node.right, level + 1, "R--- ")
            else:
                print(" " * ((level + 1) * 4) + "R--- None")

# 示例 1：右旋操作
print("示例 1: 右旋操作")
root1 = TreeNode(30)
root1.left = TreeNode(20)
root1.left.left = TreeNode(10)

print("原始树：")
print_tree(root1)

root1 = right_rotate(root1)
print("右旋操作后的树：")
print_tree(root1)
print("\n")

# 示例 2：左旋操作
print("示例 2: 左旋操作")
root2 = TreeNode(10)
root2.right = TreeNode(20)
root2.right.right = TreeNode(30)

print("原始树：")
print_tree(root2)

root2 = left_rotate(root2)
print("左旋操作后的树：")
print_tree(root2)
print("\n")

# 示例 3：左-右旋操作
print("示例 3: 左-右旋操作")
root3 = TreeNode(30)
root3.left = TreeNode(10)
root3.left.right = TreeNode(20)

print("原始树：")
print_tree(root3)

root3 = left_right_rotate(root3)
print("左-右旋操作后的树：")
print_tree(root3)
print("\n")

# 示例 4：右-左旋操作
print("示例 4: 右-左旋操作")
root4 = TreeNode(10)
root4.right = TreeNode(30)
root4.right.left = TreeNode(20)

print("原始树：")
print_tree(root4)

root4 = right_left_rotate(root4)
print("右-左旋操作后的树：")
print_tree(root4)
print("\n")
