class ArrayTree:
    def __init__(self, size):
        self.tree = [None] * size

    def set(self, index, value):
        self.tree[index] = value

    def get(self, index):
        return self.tree[index]

    def left_child_index(self, index):
        return 2 * index + 1

    def right_child_index(self, index):
        return 2 * index + 2

    def parent_index(self, index):
        return (index - 1) // 2
