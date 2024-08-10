import matplotlib.pyplot as plt

# 定义初始嵌入向量
vectors = {
    'cat': [0.1, 0.3],
    'dog': [0.5, 0.7],
    'bird': [0.2, 0.4]
}

# 创建绘图
plt.figure(figsize=(8, 6))

# 绘制每个单词的向量
for word, vector in vectors.items():
    plt.scatter(vector[0], vector[1], label=word)

# 添加标签
for word, vector in vectors.items():
    plt.annotate(word, (vector[0], vector[1]))

# 设置图形标题和轴标签
plt.title("A two-dimensional representation of an embedding vector")
plt.xlabel("Dimension1")
plt.ylabel("Dimension2")

# 显示图例
plt.legend()

# 显示图形
plt.show()
