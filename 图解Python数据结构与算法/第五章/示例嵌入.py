import numpy as np
import matplotlib.pyplot as plt
import torch
import torch.nn as nn

# 定义词汇表大小和嵌入维度
vocab_size = 3  # 词汇表大小为3 (猫、狗、鸟)
embedding_dim = 2  # 嵌入维度为2

# 创建嵌入层
embedding_layer = nn.Embedding(vocab_size, embedding_dim)

# 初始化嵌入层的权重
nn.init.uniform_(embedding_layer.weight, -1, 1)  # 在[-1, 1]范围内均匀分布

# 定义输入索引
input_indices = torch.tensor([0, 1, 2])  # 分别代表 猫、狗、鸟

# 获取嵌入向量
embedded_vectors = embedding_layer(input_indices).detach().numpy()

# 映射索引到单词
word_to_index = {0: 'cat', 1: 'dog', 2: 'bird'}

# 创建绘图
plt.figure(figsize=(8, 6))

# 绘制每个单词的向量
for idx, vector in enumerate(embedded_vectors):
    plt.scatter(vector[0], vector[1], label=word_to_index[idx])
    plt.annotate(word_to_index[idx], (vector[0], vector[1]))

# 设置图形标题和轴标签
plt.title("A two-dimensional representation of an embedding vector")
plt.xlabel("Dimension1")
plt.ylabel("Dimension2")

# 显示图例
plt.legend()

# 显示图形
plt.show()

# 输出嵌入向量的坐标
for idx, vector in enumerate(embedded_vectors):
    print(f"{word_to_index[idx]} 的嵌入向量坐标: {vector}")
