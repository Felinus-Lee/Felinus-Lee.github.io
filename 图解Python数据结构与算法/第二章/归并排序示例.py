def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # 找到中间点并分割数组
    mid = len(arr) // 2
    print(f"分割: {arr} -> 左半部分: {arr[:mid]}, 右半部分: {arr[mid:]}")
    
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # 合并排序后的子数组
    merged = merge(left_half, right_half)
    print(f"合并: 左半部分: {left_half}, 右半部分: {right_half} -> 合并结果: {merged}")
    
    return merged

def merge(left, right):
    sorted_arr = []
    i = j = 0

    # 合并两个已排序的子数组
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1

    # 添加剩余元素
    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])

    return sorted_arr

# 示例
elements = [7, 4, 1, 5]
print("初始数组:", elements)
sorted_elements = merge_sort(elements)
print("排序结果:", sorted_elements)
