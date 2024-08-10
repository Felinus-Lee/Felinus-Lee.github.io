import numpy as np
import matplotlib.pyplot as plt

# 定义 Tanh 函数
def tanh(x):
    return np.tanh(x)

# 生成 x 值
x = np.linspace(-10, 10, 400)
# 计算 y 值
y = tanh(x)

# 绘制 Tanh 函数曲线
plt.figure(figsize=(8, 6))
plt.plot(x, y, label='Tanh Function', color='blue')
plt.title('Tanh Activation Function')
plt.xlabel('Input (x)')
plt.ylabel('Output (tanh(x))')
plt.axhline(0, color='gray', lw=0.5)
plt.axhline(1, color='gray', lw=0.5)
plt.axhline(-1, color='gray', lw=0.5)
plt.axvline(0, color='gray', lw=0.5)
plt.legend()
plt.grid(True)
plt.show()
