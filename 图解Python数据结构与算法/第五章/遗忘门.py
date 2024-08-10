import numpy as np

# Sigmoid 激活函数
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# 初始化输入数据和前一时间步的隐藏状态
x_t = np.array([0])  # 第一个字符的索引为 0
h_t_minus_1 = np.array([0])  # 初始隐藏状态为 0

# 拼接隐藏状态和输入数据
combined_input = np.concatenate((h_t_minus_1, x_t))

# 初始化输入门和遗忘门的权重矩阵和偏置项
W_i = np.array([0.5, 0.5])  # 输入门权重矩阵为 0.5
W_f = np.array([0.5, 0.5])  # 遗忘门权重矩阵为 0.5
b_i = 0.1  # 输入门偏置项
b_f = 0.1  # 遗忘门偏置项

# 计算输入门和遗忘门的输出值
i_t = sigmoid(np.dot(W_i, combined_input) + b_i)
f_t = sigmoid(np.dot(W_f, combined_input) + b_f)

# 打印计算结果
print("输入门的输出值 i_t:", i_t)
print("遗忘门的输出值 f_t:", f_t)
