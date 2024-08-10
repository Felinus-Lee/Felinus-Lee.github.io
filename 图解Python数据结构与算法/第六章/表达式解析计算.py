class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def build_syntax_tree(tokens):
    # 初始化根节点
    root = TreeNode(None)
    current_node = root
    stack = []

    for token in tokens:
        if token == '(':
            # 新建左子节点，并移动当前节点到左子节点
            current_node.left = TreeNode(None)
            stack.append(current_node)
            current_node = current_node.left
        elif token == ')':
            # 返回到上一级节点
            if stack:
                current_node = stack.pop()
        elif token in ['+', '-', '*', '/']:
            # 设置当前节点的值为操作符
            current_node.value = token
            # 新建右子节点，并移动当前节点到右子节点
            current_node.right = TreeNode(None)
            stack.append(current_node)
            current_node = current_node.right
        else:
            # 设置当前节点的值为操作数
            current_node.value = int(token)
            # 如果栈非空，返回到上一级节点
            if stack:
                current_node = stack.pop()

    return root

def evaluate_syntax_tree(root):
    if root is None:
        return 0
    
    if isinstance(root.value, int):
        return root.value
    
    left_value = evaluate_syntax_tree(root.left)
    right_value = evaluate_syntax_tree(root.right)
    
    if root.value == '+':
        return left_value + right_value
    elif root.value == '-':
        return left_value - right_value
    elif root.value == '*':
        return left_value * right_value
    elif root.value == '/':
        if right_value != 0:
            return left_value / right_value
        else:
            raise ValueError("Division by zero")
    else:
        raise ValueError("Invalid operator")

# 测试代码
expression_tokens = ['(', '3', '+', '4', ')', '*', '5']
syntax_tree = build_syntax_tree(expression_tokens)
result = evaluate_syntax_tree(syntax_tree)
print("Expression result:", result)
