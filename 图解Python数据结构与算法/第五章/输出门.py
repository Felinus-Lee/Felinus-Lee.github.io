import numpy as np

# 定义 sigmoid 函数
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# 给定的参数
W_o = np.array([0.01, 0.01, 0.01, 0.01])  # 输出门的权重向量
b_o = 0.1  # 输出门的偏置项

# 假设的输入数据和前一时间步的隐藏状态
x_t = np.array([0.4, 0.5])  # 当前时间步的输入数据
h_t_minus_1 = np.array([0.3, 0.5])  # 前一时间步的隐藏状态

# 拼接隐藏状态和输入数据
combined_input = np.concatenate((h_t_minus_1, x_t))

# 计算输出门的加权和
output_gate_input = np.dot(W_o, combined_input) + b_o

# 计算输出门的输出
o_t = sigmoid(output_gate_input)

# 打印计算结果
print("输出门的输出 o_t:", o_t)

