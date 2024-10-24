def heapify(arr, n, i):
    """调整以索引 i 为根的子树，确保满足最小堆的性质"""
    smallest = i  # 假设当前节点 i 是最小值
    left = 2 * i + 1  # 左子节点索引
    right = 2 * i + 2  # 右子节点索引

    # 如果左子节点存在且小于当前节点，则更新最小值
    if left < n and arr[left] < arr[smallest]:
        smallest = left

    # 如果右子节点存在且小于当前最小值，则更新最小值
    if right < n and arr[right] < arr[smallest]:
        smallest = right

    # 如果最小值不是当前节点，进行交换，并递归调整
    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]  # 交换
        heapify(arr, n, smallest)  # 递归调整

def build_min_heap(arr):
    """构建最小堆"""
    n = len(arr)
    # 从最后一个非叶子节点开始，逐步向前调整
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

# 测试数组
arr = [3, 6, 5, 1, 8]

print("原始数组:", arr)
build_min_heap(arr)
print("构建的最小堆:", arr)
