import numpy as np

# 输入层节点数
input_layer_size = 28 * 28  # 对应于784个输入特征

# 隐藏层节点数
hidden_layer_size = 128

# 初始化权重矩阵W1，从输入层到隐藏层
# 形状为 (隐藏层节点数, 输入层节点数)
W1 = np.random.rand(hidden_layer_size, input_layer_size)

# 打印权重矩阵的形状和一个示例
print("权重矩阵W1的形状：", W1.shape)
print("权重矩阵W1的示例值：", W1)

# 示例输入数据（28x28像素的灰度图像展平为一维向量）
input_data = np.random.rand(input_layer_size)

# 计算隐藏层输入：加权和
# 矩阵乘法：隐藏层输入 = 权重矩阵W1 × 输入数据
hidden_layer_input = np.dot(W1, input_data)

# 偏置向量
b1 = np.random.rand(hidden_layer_size)

# 加上偏置
hidden_layer_input += b1

# 激活函数（例如ReLU）
def relu(x):
    return np.maximum(0, x)

# 计算隐藏层输出
hidden_layer_output = relu(hidden_layer_input)

# 打印隐藏层输入和输出的示例值
print("隐藏层输入的示例值：", hidden_layer_input)
print("隐藏层输出的示例值：", hidden_layer_output)
