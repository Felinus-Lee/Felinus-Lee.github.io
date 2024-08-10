import numpy as np
import matplotlib.pyplot as plt

# 定义逻辑函数（S形函数）
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# 生成一些示例数据
x = np.linspace(-5, 5, 100)
y = sigmoid(x)

# 绘制曲线
plt.plot(x, y, label='Sigmoid Curve', color='blue')
plt.xlabel('x')
plt.ylabel('Sigmoid(x)')
plt.title('Logistic Regression Sigmoid Curve')
plt.legend()
plt.grid(True)
plt.show()
