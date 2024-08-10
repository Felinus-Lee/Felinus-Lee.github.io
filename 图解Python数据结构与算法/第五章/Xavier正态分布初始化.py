import numpy as np

def xavier_normal_init(size):
    n_in, n_out = size
    stddev = np.sqrt(2 / (n_in + n_out))
    return np.random.randn(*size) * stddev

# 示例：初始化一个形状为(3, 2)的权重矩阵
W1 = xavier_normal_init((3, 2))
print(W1)
