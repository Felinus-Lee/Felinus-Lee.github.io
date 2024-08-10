from keras.models import Sequential
from keras.layers import Dense

# 创建一个顺序模型
model = Sequential()

# 添加输入层和第一个隐藏层，使用默认的偏置向量
model.add(Dense(units=32, input_dim=64, activation='relu'))

# 添加输出层，使用默认的偏置向量
model.add(Dense(units=10, activation='softmax'))

# 编译模型
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
