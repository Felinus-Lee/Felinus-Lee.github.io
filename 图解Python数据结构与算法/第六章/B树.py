class BTreeNode:
    def __init__(self, t, leaf=False):
        self.t = t          # 最小度数（阶）
        self.leaf = leaf    # 是否为叶子节点
        self.keys = []      # 存储关键字
        self.children = []  # 存储子节点

class BTree:
    def __init__(self, t):
        self.root = BTreeNode(t, True)
        self.t = t

    def traverse(self, node, level=0):
        print("Level", level, ":", node.keys)
        if not node.leaf:
            for child in node.children:
                self.traverse(child, level + 1)

    def search(self, node, key):
        i = 0
        while i < len(node.keys) and key > node.keys[i]:
            i += 1
        if i < len(node.keys) and key == node.keys[i]:
            return True
        if node.leaf:
            return False
        return self.search(node.children[i], key)

    def insert(self, key):
        root = self.root
        if len(root.keys) == (2 * self.t - 1):
            s = BTreeNode(self.t, False)
            self.root = s
            s.children.append(root)
            self.split_child(s, 0)
            self.insert_non_full(s, key)
        else:
            self.insert_non_full(root, key)

    def insert_non_full(self, node, key):
        i = len(node.keys) - 1
        if node.leaf:
            node.keys.append(None)
            while i >= 0 and key < node.keys[i]:
                node.keys[i + 1] = node.keys[i]
                i -= 1
            node.keys[i + 1] = key
        else:
            while i >= 0 and key < node.keys[i]:
                i -= 1
            i += 1
            if len(node.children[i].keys) == (2 * self.t - 1):
                self.split_child(node, i)
                if key > node.keys[i]:
                    i += 1
            self.insert_non_full(node.children[i], key)

    def split_child(self, parent, index):
        t = self.t
        y = parent.children[index]
        z = BTreeNode(t, y.leaf)
        parent.children.insert(index + 1, z)
        parent.keys.insert(index, y.keys[t - 1])
        z.keys = y.keys[t:(2 * t - 1)]
        y.keys = y.keys[0:(t - 1)]
        if not y.leaf:
            z.children = y.children[t:(2 * t)]
            y.children = y.children[0:t]