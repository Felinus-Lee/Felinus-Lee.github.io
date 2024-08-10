class BinaryTree:
    def __init__(self):
        self.tree = []

    def add(self, value):
        self.tree.append(value)

    def get_left_child_index(self, index):
        left_index = 2 * index + 1
        return left_index if left_index < len(self.tree) else None

    def get_right_child_index(self, index):
        right_index = 2 * index + 2
        return right_index if right_index < len(self.tree) else None

    def get_parent_index(self, index):
        if index == 0:
            return None
        return (index - 1) // 2

    def display(self):
        for i, value in enumerate(self.tree):
            print(f"Index: {i}, Value: {value}")

# 创建二叉树并添加节点
bt = BinaryTree()
nodes = ['A', 'B', 'C', 'D', 'E']
for node in nodes:
    bt.add(node)

# 打印二叉树
bt.display()

# 示例：获取某个节点的左、右子节点和父节点的索引
index = 1  # 节点 B
left_child_index = bt.get_left_child_index(index)
right_child_index = bt.get_right_child_index(index)
parent_index = bt.get_parent_index(index)

print(f"Node at index {index}: {bt.tree[index]}")
print(f"Left child index: {left_child_index}, Value: {bt.tree[left_child_index] if left_child_index is not None else 'None'}")
print(f"Right child index: {right_child_index}, Value: {bt.tree[right_child_index] if right_child_index is not None else 'None'}")
print(f"Parent index: {parent_index}, Value: {bt.tree[parent_index] if parent_index is not None else 'None'}")
