import numpy as np
import matplotlib.pyplot as plt

def get_position_encoding(seq_len, d_model):
    # 创建一个矩阵，其中seq_len是序列长度，d_model是嵌入维度
    position_encoding = np.zeros((seq_len, d_model))
    
    # 计算每个位置的编码值
    for pos in range(seq_len):
        for i in range(0, d_model, 2):
            position_encoding[pos, i] = np.sin(pos / (10000 ** ((2 * i) / d_model)))
            if i + 1 < d_model:
                position_encoding[pos, i + 1] = np.cos(pos / (10000 ** ((2 * i) / d_model)))
    
    return position_encoding

# 示例参数
seq_len = 50  # 序列长度
d_model = 512  # 嵌入维度

# 获取位置编码
position_encoding = get_position_encoding(seq_len, d_model)

# 可视化位置编码
plt.figure(figsize=(10, 8))
plt.imshow(position_encoding, aspect='auto', cmap='viridis')
plt.colorbar()
plt.title("Location coding")
plt.xlabel("Embedding dimensions")
plt.ylabel("Sequence position")
plt.show()
