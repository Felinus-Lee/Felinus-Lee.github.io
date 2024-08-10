import torch
import torch.nn as nn

# 假设词汇表大小为10000，每个单词映射为长度为512的向量
vocab_size = 10000
embedding_dim = 512

# 定义嵌入层
embedding_layer = nn.Embedding(vocab_size, embedding_dim)

# 示例输入
input_tokens = torch.LongTensor([[1, 2, 3, 4, 5]])

# 将输入token映射为向量表示
embedded_tokens = embedding_layer(input_tokens)

print("Embedded tokens shape:", embedded_tokens.shape)  # 输出：torch.Size([1, 5, 512])
