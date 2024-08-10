def karatsuba(x, y):
    # 判断输入的数字是否为单个数字
    if x < 10 and y < 10:
        return x * y
    
    # 计算数字的位数
    n = max(len(str(x)), len(str(y)))
    half_n = n // 2
    
    # 分解数字为两部分
    a = x // 10 ** half_n
    b = x % (10 ** half_n)
    c = y // 10 ** half_n
    d = y % (10 ** half_n)
    
    # 递归计算三个乘积
    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    ad_bc = karatsuba(a + b, c + d) - ac - bd
    
    # 合并乘积得到结果
    result = ac * (10 ** (2 * half_n)) + ad_bc * (10 ** half_n) + bd
    
    return result

# 测试
x = 13
y = 24
print("Result:", karatsuba(x, y))
