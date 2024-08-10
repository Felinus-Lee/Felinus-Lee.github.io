class BPlusTreeNode:
    def __init__(self, t, leaf=False):
        self.t = t  # 最小度数
        self.leaf = leaf  # 是否为叶子节点
        self.keys = []  # 存储键
        self.children = []  # 存储子节点
        self.next = None  # 叶子节点链表指针，用于顺序访问叶子节点

class BPlusTree:
    def __init__(self, t):
        self.t = t  # 最小度数
        self.root = BPlusTreeNode(t, True)  # 创建根节点，初始时为叶子节点

    def insert(self, key):
        root = self.root
        if len(root.keys) == (2 * self.t - 1):  # 根节点已满
            s = BPlusTreeNode(self.t, False)  # 创建新根节点
            self.root = s
            s.children.append(root)  # 将旧根节点作为新根的子节点
            self.split_child(s, 0)  # 分裂旧根节点
            self.insert_non_full(s, key)  # 在新根节点中插入键
        else:
            self.insert_non_full(root, key)

    def insert_non_full(self, x, key):
        if x.leaf:
            x.keys.append(None)  # 增加一个位置来插入新键
            i = len(x.keys) - 2
            while i >= 0 and key < x.keys[i]:
                x.keys[i + 1] = x.keys[i]
                i -= 1
            x.keys[i + 1] = key
            if x.next is None:
                x.next = None  # 如果是新的叶子节点，没有链接到下一个叶子节点
            else:
                x.next = x.next  # 更新叶子节点链表的链接
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
        if y.leaf:
            z.next = y.next
            y.next = z

    def search(self, k):
        x = self.root
        while not x.leaf:
            i = 0
            while i < len(x.keys) and k > x.keys[i]:
                i += 1
            x = x.children[i]
        return k in x.keys

# 示例代码使用
if __name__ == "__main__":
    t = 3  # B+树的最小度数
    b_plus_tree = BPlusTree(t)
    
    # 插入键
    keys = [10, 20, 5, 6, 15, 30, 25, 50, 40, 60, 45]
    for key in keys:
        b_plus_tree.insert(key)
    
    # 搜索键
    search_keys = [15, 25, 40, 70]
    for key in search_keys:
        result = b_plus_tree.search(key)
        print(f"Key {key} {'found' if result else 'not found'} in B+ tree.")
