def binary_search(arr):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2  # 计算中间索引
        mid_value = arr[mid]  # 获取中间索引对应的元素值
        
        if mid_value == 1:
            return mid  # 如果中间元素为1，返回索引
        elif mid_value < 1:
            left = mid + 1  # 如果中间元素小于1，缩小搜索范围到右半部分
        else:
            right = mid - 1  # 如果中间元素大于1，缩小搜索范围到左半部分
    
    return -1  # 如果数组中不存在元素为1，返回-1