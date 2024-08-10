import numpy as np

# 定义双曲正切函数
def tanh(x):
    return np.tanh(x)

# 给定的输入门和遗忘门的输出值
i_t = 0.52497918747894
f_t = 0.52497918747894

# 初始化输入数据和前一时间步的隐藏状态
x_t = np.array([0])  # 假设第一个字符的索引为 0
h_t_minus_1 = np.array([0])  # 初始隐藏状态为 0

# 初始化候选记忆单元的权重矩阵和偏置项
W_c = np.array([0.5, 0.5])  # 候选记忆单元权重矩阵
b_c = 0.1  # 候选记忆单元偏置项

# 拼接隐藏状态和输入数据
combined_input = np.concatenate((h_t_minus_1, x_t))

# 计算候选记忆单元的值
tilde_C_t = tanh(np.dot(W_c, combined_input) + b_c)

# 打印计算结果
print("候选记忆单元的值 tilde_C_t:", tilde_C_t)
