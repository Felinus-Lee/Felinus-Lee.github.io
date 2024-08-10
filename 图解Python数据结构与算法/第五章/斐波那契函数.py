def factorial(n):
    # 递归基本情况：当 n 等于 0 或 1 时，阶乘为 1。
    if n == 0 or n == 1:
        return 1
    # 递归规则：阶乘的递归定义为 n * (n-1)!
    return n * factorial(n - 1)

# 测试递归函数
print(factorial(5))  # 输出 120，即 5 的阶乘
