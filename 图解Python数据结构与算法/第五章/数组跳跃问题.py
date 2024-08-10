def can_jump(nums):
    max_reachable = 0  # 当前能够到达的最远位置
    n = len(nums)
    
    for i in range(n):
        if i > max_reachable:
            return False  # 无法到达当前位置
        max_reachable = max(max_reachable, i + nums[i])  # 更新当前能够到达的最远位置
        if max_reachable >= n - 1:  # 如果最远位置能够到达数组的最后一个位置，则返回True
            return True
    
    return False

# 测试
nums = [2, 3, 5, 7, 6, 1, 3]
print(can_jump(nums))  # 输出 True
