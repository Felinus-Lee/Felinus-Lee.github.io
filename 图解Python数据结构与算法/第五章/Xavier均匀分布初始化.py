import numpy as np

def xavier_uniform_init(size):
    n_in, n_out = size
    limit = np.sqrt(6 / (n_in + n_out))
    return np.random.uniform(-limit, limit, size=size)

# 示例：初始化一个形状为(3, 2)的权重矩阵
W1 = xavier_uniform_init((3, 2))
print(W1)
