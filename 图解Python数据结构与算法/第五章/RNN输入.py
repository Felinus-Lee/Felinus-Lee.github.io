import numpy as np
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

# 示例古诗数据
poems = [
    "春眠不觉晓，处处闻啼鸟。",
    "夜来风雨声，花落知多少。",
    "床前明月光，疑是地上霜。",
    "举头望明月，低头思故乡。"
]

# 将文本转换为序列数据
tokenizer = Tokenizer(char_level=True)  # 逐字级别
tokenizer.fit_on_texts(poems)
sequences = tokenizer.texts_to_sequences(poems)
word_index = tokenizer.word_index

# 生成输入序列和目标
maxlen = 5  # 序列长度
X = []
y = []

for seq in sequences:
    for i in range(1, len(seq)):
        input_seq = seq[:i]
        target = seq[i]
        X.append(input_seq)
        y.append(target)

# 填充序列
X = pad_sequences(X, maxlen=maxlen)
y = np.array(y)

# 打印数据
print("Tokenized sequences:")
for i, sequence in enumerate(X):
    target = y[i]
    print(f"Input sequence: {sequence}, Target: {target}")
