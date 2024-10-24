def factorial(n):
    # 打印递归进入的情况
    print(f"Entering factorial({n})")
    
    # 基本情况：n为1时停止递归
    if n == 1:
        print(f"Returning 1 from factorial({n})")  # 基本情况直接返回1
        return 1
    else:
        # 递归调用，继续向下分解问题
        result = n * factorial(n - 1)
        
        # 打印回溯阶段，返回上一级的结果
        print(f"Returning {result} from factorial({n})")
        return result

# 调用计算5的阶乘
print(f"Factorial of 5 is: {factorial(5)}")
