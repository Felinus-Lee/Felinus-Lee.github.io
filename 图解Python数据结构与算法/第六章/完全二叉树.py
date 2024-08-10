class CompleteBinaryTree:
    def __init__(self):
        self.tree = []

    def insert(self, value):
        """插入新节点"""
        self.tree.append(value)
        self._heapify_up(len(self.tree) - 1)

    def delete(self):
        """删除根节点并返回它的值"""
        if len(self.tree) == 0:
            return None
        if len(self.tree) == 1:
            return self.tree.pop()
        root_value = self.tree[0]
        self.tree[0] = self.tree.pop()  # 用最后一个节点替换根节点
        self._heapify_down(0)
        return root_value

    def _heapify_up(self, index):
        """向上调整节点位置以保持堆的性质"""
        parent_index = (index - 1) // 2
        while index > 0 and self.tree[index] > self.tree[parent_index]:
            self.tree[index], self.tree[parent_index] = self.tree[parent_index], self.tree[index]
            index = parent_index
            parent_index = (index - 1) // 2

    def _heapify_down(self, index):
        """向下调整节点位置以保持堆的性质"""
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        largest = index
        if left_child_index < len(self.tree) and self.tree[left_child_index] > self.tree[largest]:
            largest = left_child_index
        if right_child_index < len(self.tree) and self.tree[right_child_index] > self.tree[largest]:
            largest = right_child_index
        if largest != index:
            self.tree[index], self.tree[largest] = self.tree[largest], self.tree[index]
            self._heapify_down(largest)

    def display(self):
        """显示树的结构"""
        if not self.tree:
            print("Tree is empty")
            return
        levels = []
        level = 0
        while (2 ** level - 1) < len(self.tree):
            levels.append(self.tree[2 ** level - 1:2 ** (level + 1) - 1])
            level += 1
        for l in levels:
            print(" ".join(map(str, l)))

# 示例用法
cbt = CompleteBinaryTree()
cbt.insert(10)
cbt.insert(20)
cbt.insert(5)
cbt.insert(6)
cbt.insert(1)
cbt.insert(8)
cbt.insert(9)

print("树结构:")
cbt.display()

print("\n删除根节点:")
cbt.delete()
cbt.display()
