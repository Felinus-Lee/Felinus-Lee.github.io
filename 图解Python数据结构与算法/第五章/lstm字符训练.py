import numpy as np  
from tensorflow.keras.models import Sequential  
from tensorflow.keras.layers import LSTM, Dense  
  
# 自定义字符到索引的映射  
char_to_index = {'h': 0, 'e': 1, 'l': 2, 'o': 3}  
index_to_char = np.array(['h', 'e', 'l', 'o'])  
  
text = "hello"  
  
# 准备训练数据  
sequence_length = 3  
dataX = []  
dataY = []  
for i in range(0, len(text) - sequence_length, 1):  
    seq_in = text[i:i + sequence_length]  
    seq_out = text[i + sequence_length]  
    dataX.append([char_to_index[char] for char in seq_in])  
    dataY.append(char_to_index[seq_out])  
  

n_patterns = len(dataX)  
X = np.reshape(dataX, (n_patterns, sequence_length, 1))  
y = np.array(dataY)  
  
# 定义模型  
model = Sequential()  
model.add(LSTM(50, input_shape=(X.shape[1], X.shape[2])))  
model.add(Dense(len(char_to_index), activation='softmax'))  
  
model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])  

model.fit(X, y, epochs=100, batch_size=1, verbose=2)  
  
# 示例预测
test_seq = np.array([[char_to_index[c] for c in 'hel']])  
test_seq = np.reshape(test_seq, (1, sequence_length, 1))  
prediction = model.predict(test_seq, verbose=0)  
predicted_char = index_to_char[np.argmax(prediction)]  
print("Predicted next character:", predicted_char)  
  