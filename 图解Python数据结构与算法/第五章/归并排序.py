def merge_and_sort(a, b):
    merged_array = []  # 创建一个空数组用于存放合并后的结果
    i = len(a) - 1  # 初始化a数组的指针，从末尾开始
    j = len(b) - 1  # 初始化b数组的指针，从末尾开始

    # 循环直到a和b数组的指针都大于等于0
    while i >= 0 and j >= 0:
        if a[i] > b[j]:
            merged_array.append(a[i])  # 将a中较大的元素添加到合并数组中
            i -= 1
        else:
            merged_array.append(b[j])  # 将b中较大的元素添加到合并数组中
            j -= 1

    # 将剩余未处理的元素添加到合并数组中
    while i >= 0:
        merged_array.append(a[i])
        i -= 1
    while j >= 0:
        merged_array.append(b[j])
        j -= 1

    # 返回合并后的数组
    return merged_array

# 示例
a = [6, 3]
b = [8, 1]
merged_and_sorted = merge_and_sort(a, b)
print("Merged and sorted array:", merged_and_sorted)
