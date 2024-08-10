import numpy as np
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense

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

# 构建模型
vocab_size = len(word_index) + 1  # 词汇表大小加1
embedding_dim = 50  # 嵌入维度

model = Sequential()
model.add(Embedding(input_dim=vocab_size, output_dim=embedding_dim, input_length=maxlen))
model.add(LSTM(units=128))  # 隐藏层
model.add(Dense(units=vocab_size, activation='softmax'))  # 输出层

# 编译模型
model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# 打印模型摘要
model.summary()

# 训练模型
model.fit(X, y, epochs=50, batch_size=32)

# 预测下一个字符
def predict_next_chars(model, tokenizer, text, num_chars=5, maxlen=5):
    result = []
    for _ in range(num_chars):
        # 将输入文本转换为序列
        sequences = tokenizer.texts_to_sequences([text])
        # 填充序列
        padded_seq = pad_sequences(sequences, maxlen=maxlen)
        # 预测下一个字符的概率分布
        pred = model.predict(padded_seq, verbose=0)
        # 获取概率最高的字符索引
        next_index = np.argmax(pred)
        # 获取对应字符
        for char, index in tokenizer.word_index.items():
            if index == next_index:
                result.append(char)
                text += char
                text = text[1:]  # 保持长度为maxlen
                break
    return ''.join(result)

# 示例预测
input_text = "举头望明月"
predicted_chars = predict_next_chars(model, tokenizer, input_text[-maxlen:], num_chars=5)
print(f"Input text: {input_text}")
print(f"Predicted next characters: {predicted_chars}")
