import random
import time

def bfs(array):
    result = []
    queue = [array[0]]  # 用列表模拟队列，并将根节点放入队列中
    index = 1  # 当前遍历到的数组索引

    while queue:
        node = queue.pop(0)  # 出队
        result.append(node)  # 将出队的节点添加到结果中

        left_child_index = 2 * index  # 左孩子节点的索引
        right_child_index = 2 * index + 1  # 右孩子节点的索引

        if left_child_index <= len(array):  # 检查左孩子节点是否在数组范围内
            queue.append(array[left_child_index - 1])  # 将左孩子节点入队

        if right_child_index <= len(array):  # 检查右孩子节点是否在数组范围内
            queue.append(array[right_child_index - 1])  # 将右孩子节点入队

        index += 1  # 更新当前遍历到的数组索引

    return result

# 生成100个随机数并转化为数组
random_numbers = [random.randint(0, 1000) for _ in range(999)]

# 测量函数运行时间
start_time = time.time()
result = bfs(random_numbers)
end_time = time.time()

# 计算运行时间
running_time = end_time - start_time
print("BFS 运行时间: {:.6f} 秒".format(running_time))