import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from sklearn.preprocessing import MinMaxScaler

# 生成一些示例数据（模拟股票价格）
def generate_data(n):
    time = np.arange(0, n, 1)
    data = np.sin(time * 0.1) + np.random.normal(0, 0.1, size=n)
    return data.reshape(-1, 1)

# 数据预处理
def preprocess_data(data, look_back):
    scaler = MinMaxScaler(feature_range=(0, 1))
    data_normalized = scaler.fit_transform(data)
    X, y = [], []
    for i in range(len(data_normalized) - look_back):
        X.append(data_normalized[i:(i + look_back), 0])
        y.append(data_normalized[i + look_back, 0])
    return np.array(X), np.array(y), scaler

# 定义模型
def create_lstm_model(look_back):
    model = Sequential()
    model.add(LSTM(units=50, input_shape=(look_back, 1)))
    model.add(Dense(units=1))
    model.compile(optimizer='adam', loss='mean_squared_error')
    return model

# 生成示例数据
np.random.seed(42)
data = generate_data(1000)

# 数据预处理及分割
look_back = 10
X, y, scaler = preprocess_data(data, look_back)
X = np.reshape(X, (X.shape[0], X.shape[1], 1))

# 创建并训练模型
model = create_lstm_model(look_back)
model.fit(X, y, epochs=50, batch_size=32, verbose=1)

# 预测未来值
predicted_values = []
last_sequence = X[-1].flatten().tolist()

for i in range(100):
    last_sequence_np = np.array(last_sequence[-look_back:], dtype=np.float32)  # 只取最后的look_back个数据作为输入
    last_sequence_reshaped = last_sequence_np.reshape(1, look_back, 1)
    next_predicted_value = model.predict(last_sequence_reshaped, verbose=0)
    predicted_values.append(next_predicted_value[0, 0])
    last_sequence.append(next_predicted_value[0, 0])

# 反向转换预测值
predicted_values = scaler.inverse_transform(np.array(predicted_values).reshape(-1, 1))

# 绘制预测结果
plt.figure(figsize=(10, 6))
plt.plot(np.arange(len(data)), data, label='Original Data')
plt.plot(np.arange(len(data), len(data) + len(predicted_values)), predicted_values, label='Predicted Data')
plt.xlabel('Time')
plt.ylabel('Value')
plt.title('LSTM Time Series Prediction')
plt.legend()
plt.show()
