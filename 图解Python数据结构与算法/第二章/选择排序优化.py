def optimized_selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # 假设当前数组已经排序
        is_sorted = True
        min_index = i
        
        # 找到未排序部分的最小元素
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        # 如果最小元素不是当前元素，进行交换
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            is_sorted = False
        
        # 如果没有发生交换，数组已经是有序的
        if is_sorted:
            break

    return arr

# 示例用法
array = [2, 3, 5, 6, 7]
sorted_array = optimized_selection_sort(array)
print(sorted_array)  # 输出: [2, 3, 5, 6, 7]
