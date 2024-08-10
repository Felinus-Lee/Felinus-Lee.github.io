import numpy as np

def random_init(size, scale=0.01):
    return np.random.randn(*size) * scale

# 示例：初始化一个形状为(2, 3)的权重矩阵
W1 = random_init((2, 3))
print(W1)
