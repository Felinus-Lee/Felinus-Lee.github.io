class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class DoublyListNode:
    def __init__(self, value=0, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

def tree_to_doubly_list(root):
    if not root:
        return None

    def inorder_traversal(node):
        nonlocal last, head
        if not node:
            return
        inorder_traversal(node.left)  # 递归遍历左子树
        if last:
            # 连接当前节点与前一个节点
            last.next = DoublyListNode(node.value)
            last.next.prev = last
            last = last.next
        else:
            # 初始化头节点
            head = DoublyListNode(node.value)
            last = head
        inorder_traversal(node.right)  # 递归遍历右子树

    last, head = None, None
    inorder_traversal(root)
    return head

# 示例树
#       4
#      / \
#     2   5
#    / \
#   1   3

# 创建树节点
root = TreeNode(4)
root.left = TreeNode(2, TreeNode(1), TreeNode(3))
root.right = TreeNode(5)

# 将树转换为双向链表
head = tree_to_doubly_list(root)

# 打印双向链表
current = head
while current:
    print(current.value, end=' <-> ' if current.next else '\n')
    current = current.next
