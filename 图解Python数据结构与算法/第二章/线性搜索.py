def linear_search_with_steps(arr, target):
    """
    带有搜索过程展示的线性搜索算法实现

    参数：
    - arr: 包含要搜索的元素的列表
    - target: 要搜索的目标元素

    返回：
    - 如果目标元素在列表中，返回目标元素的索引；否则，返回 -1。
    """
    for i in range(len(arr)):
        print(f"当前指针位置: {i}, 当前元素: {arr[i]}")

        if arr[i] == target:
            print(f"找到目标元素 {target}，索引为 {i}")
            return i  # 找到目标元素，返回索引

        print(f"目标元素 {target} 与当前元素 {arr[i]} 不匹配，继续搜索...\n")

    print(f"目标元素 {target} 不在列表中")
    return -1  # 目标元素不在列表中，返回 -1

# 示例
my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
target_element = 5

result = linear_search_with_steps(my_list, target_element)