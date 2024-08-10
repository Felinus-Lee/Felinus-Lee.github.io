import heapq

class CompleteBinaryTree:
    def __init__(self):
        self.tree = []

    def insert(self, value):
        """插入新节点"""
        heapq.heappush(self.tree, value)

    def delete(self):
        """删除根节点并返回它的值"""
        if len(self.tree) == 0:
            return None
        return heapq.heappop(self.tree)

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
