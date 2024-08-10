import numpy as np
import matplotlib.pyplot as plt

# 定义 ReLU 函数
def relu(x):
    return np.maximum(0, x)

# 生成 x 值
x = np.linspace(-10, 10, 400)
# 计算 y 值
y = relu(x)

# 绘制 ReLU 函数曲线
plt.figure(figsize=(8, 6))
plt.plot(x, y, label='ReLU Function', color='blue')
plt.title('ReLU Activation Function')
plt.xlabel('Input (x)')
plt.ylabel('Output (ReLU(x))')
plt.axhline(0, color='gray', lw=0.5)
plt.axvline(0, color='gray', lw=0.5)
plt.legend()
plt.grid(True)
plt.show()
