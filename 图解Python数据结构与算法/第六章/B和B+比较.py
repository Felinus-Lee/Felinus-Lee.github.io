import random
import timeit

class BTreeNode:
    def __init__(self, t, leaf=False):
        self.t = t  # 最小度数
        self.leaf = leaf  # 是否为叶子节点
        self.keys = []  # 存储键
        self.children = []  # 存储子节点

class BTree:
    def __init__(self, t):
        self.root = BTreeNode(t, True)
        self.t = t  # 最小度数

    def insert(self, key):
        root = self.root
        if len(root.keys) == (2 * self.t - 1):  # 根节点已满
            s = BTreeNode(self.t, False)  # 创建新根节点
            self.root = s
            s.children.append(root)  # 将旧根节点作为新根的子节点
            self.split_child(s, 0)
            self.insert_non_full(s, key)
        else:
            self.insert_non_full(root, key)

    def insert_non_full(self, x, key):
        i = len(x.keys) - 1
        if x.leaf:
            x.keys.append(None)
            while i >= 0 and key < x.keys[i]:
                x.keys[i + 1] = x.keys[i]
                i -= 1
            x.keys[i + 1] = key
        else:
            while i >= 0 and key < x.keys[i]:
                i -= 1
            i += 1
            if len(x.children[i].keys) == (2 * self.t - 1):
                self.split_child(x, i)
                if key > x.keys[i]:
                    i += 1
            self.insert_non_full(x.children[i], key)

    def split_child(self, x, i):
        t = self.t
        y = x.children[i]
        z = BTreeNode(t, y.leaf)
        x.children.insert(i + 1, z)
        x.keys.insert(i, y.keys[t - 1])
        z.keys = y.keys[t:]
        y.keys = y.keys[:t - 1]
        if not y.leaf:
            z.children = y.children[t:]
            y.children = y.children[:t]

    def search(self, k, x=None):
        if x is None:
            x = self.root
        i = 0
        while i < len(x.keys) and k > x.keys[i]:
            i += 1
        if i < len(x.keys) and k == x.keys[i]:
            return True
        if x.leaf:
            return False
        return self.search(k, x.children[i])

class BPlusTreeNode:
    def __init__(self, t, leaf=False):
        self.t = t  # 最小度数
        self.leaf = leaf  # 是否为叶子节点
        self.keys = []  # 存储键
        self.children = []  # 存储子节点

class BPlusTree:
    def __init__(self, t):
        self.t = t  # 最小度数
        self.root = BPlusTreeNode(t, True)
        self.leaf_nodes = []  # 存储所有叶子节点

    def insert(self, key):
        root = self.root
        if len(root.keys) == (2 * self.t - 1):  # 根节点已满
            s = BPlusTreeNode(self.t, False)  # 创建新根节点
            self.root = s
            s.children.append(root)  # 将旧根节点作为新根的子节点
            self.split_child(s, 0)
            self.insert_non_full(s, key)
        else:
            self.insert_non_full(root, key)

    def insert_non_full(self, x, key):
        if x.leaf:
            x.keys.append(None)
            i = len(x.keys) - 2
            while i >= 0 and key < x.keys[i]:
                x.keys[i + 1] = x.keys[i]
                i -= 1
            x.keys[i + 1] = key
            self.leaf_nodes.append(x)
        else:
            i = len(x.keys) - 1
            while i >= 0 and key < x.keys[i]:
                i -= 1
            i += 1
            if len(x.children[i].keys) == (2 * self.t - 1):
                self.split_child(x, i)
                if key > x.keys[i]:
                    i += 1
            self.insert_non_full(x.children[i], key)

    def split_child(self, x, i):
        t = self.t
        y = x.children[i]
        z = BPlusTreeNode(t, y.leaf)
        x.children.insert(i + 1, z)
        x.keys.insert(i, y.keys[t - 1])
        z.keys = y.keys[t:]
        y.keys = y.keys[:t - 1]
        if not y.leaf:
            z.children = y.children[t:]
            y.children = y.children[:t]

    def search(self, k):
        x = self.root
        while not x.leaf:
            i = 0
            while i < len(x.keys) and k > x.keys[i]:
                i += 1
            x = x.children[i]
        return k in x.keys

def measure_time(func, *args, **kwargs):
    num_repeats = 3  # 重复次数
    total_time = timeit.timeit(lambda: func(*args, **kwargs), number=num_repeats)
    return total_time / num_repeats

def compare_trees():
    t = 3
    b_tree = BTree(t)
    b_plus_tree = BPlusTree(t)
    num_elements = 100000  # 使用较小的数据集
    elements = [random.randint(0, 10000000) for _ in range(num_elements)]

    # Measure B-tree insertion time
    def insert_btree():
        for elem in elements:
            b_tree.insert(elem)
    print("Measuring B-tree insertion time...")
    b_tree_time = measure_time(insert_btree)
    
    # Measure B+ tree insertion time
    def insert_bplustree():
        for elem in elements:
            b_plus_tree.insert(elem)
    print("Measuring B+ tree insertion time...")
    b_plus_tree_time = measure_time(insert_bplustree)

    # Measure B-tree search time
    search_element = elements[random.randint(0, num_elements - 1)]
    def search_btree():
        b_tree.search(search_element)
    print("Measuring B-tree search time...")
    b_tree_search_time = measure_time(search_btree)

    # Measure B+ tree search time
    def search_bplustree():
        b_plus_tree.search(search_element)
    print("Measuring B+ tree search time...")
    b_plus_tree_search_time = measure_time(search_bplustree)

    print(f"B-tree insertion time: {b_tree_time:.6f} seconds")
    print(f"B+ tree insertion time: {b_plus_tree_time:.6f} seconds")
    print(f"B-tree search time: {b_tree_search_time:.6f} seconds")
    print(f"B+ tree search time: {b_plus_tree_search_time:.6f} seconds")

if __name__ == "__main__":
    compare_trees()
