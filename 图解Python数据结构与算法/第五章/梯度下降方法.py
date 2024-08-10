import numpy as np
import matplotlib.pyplot as plt

# 定义函数
def f(x):
    return x**2

# 定义函数的导数
def df(x):
    return 2 * x

# 梯度下降算法
def gradient_descent(learning_rate, num_iterations, initial_x):
    x = initial_x
    history = [x]
    for i in range(num_iterations):
        gradient = df(x)
        x = x - learning_rate * gradient
        history.append(x)
    return history

# 设置学习率和迭代次数
learning_rate = 0.1
num_iterations = 10
initial_x = 2  # 初始点的选择可能会影响到最终的收敛结果

# 执行梯度下降算法
history = gradient_descent(learning_rate, num_iterations, initial_x)

# 绘制函数图像
x_values = np.linspace(-5, 5, 100)
y_values = f(x_values)
plt.plot(x_values, y_values, label='f(x) = x^2', color='blue')

# 绘制梯度下降路径
for i in range(len(history)-1):
    plt.plot([history[i], history[i+1]], [f(history[i]), f(history[i+1])], marker='o', color='red')

plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Gradient Descent on f(x) = x^2')
plt.grid(True)
plt.legend()
plt.show()
