def binary_search(dictionary, target):
    left, right = 0, len(dictionary) - 1
    
    while left <= right:
        mid = (left + right) // 2
        mid_value = dictionary[mid]
        
        # 比较中间值和目标值
        if mid_value == target:
            return mid  # 找到目标值，返回其索引
        elif mid_value < target:
            left = mid + 1  # 目标值在右半部分
        else:
            right = mid - 1  # 目标值在左半部分
    
    return -1  # 如果目标值不在字典中，返回 -1

# 测试代码
dictionary = ["apple", "banana", "cat", "dog", "elephant", "giraffe", "horse"]
target_word = "search"
result = binary_search(dictionary, target_word)

if result != -1:
    print(f"单词 '{target_word}' 在字典中的索引是: {result}")
else:
    print(f"单词 '{target_word}' 不在字典中")
