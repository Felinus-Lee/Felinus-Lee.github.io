class TreeNode:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def evaluate_expression_tree(root):
    if not root:
        return 0
    
    if not root.left and not root.right:
        return int(root.value)
    
    left_val = evaluate_expression_tree(root.left)  # 递归求左子树的值
    right_val = evaluate_expression_tree(root.right)  # 递归求右子树的值
    
    if root.value == '+':
        return left_val + right_val
    elif root.value == '-':
        return left_val - right_val
    elif root.value == '*':
        return left_val * right_val
    elif root.value == '/':
        return left_val / right_val

# 创建表达式树 ((4+5)*(6-3))
root = TreeNode('*')
root.left = TreeNode('+', TreeNode('4'), TreeNode('5'))
root.right = TreeNode('-', TreeNode('6'), TreeNode('3'))

# 计算表达式树的值
print(f"The value of the expression is: {evaluate_expression_tree(root)}")  # 输出: 27
