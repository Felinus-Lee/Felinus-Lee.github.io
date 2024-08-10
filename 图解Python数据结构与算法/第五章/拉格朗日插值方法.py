import numpy as np
import matplotlib.pyplot as plt

# 定义拉格朗日函数
def lagrange(x, points):
    result = 0
    n = len(points)
    for j in range(n):
        term = points[j][1]
        for k in range(n):
            if k != j:
                term *= (x - points[k][0]) / (points[j][0] - points[k][0])
        result += term
    return result

# 生成数据点
points = [(1, 2), (2, 3), (3, 5), (4, 7)]

# 绘制原始数据点
x_vals = [p[0] for p in points]
y_vals = [p[1] for p in points]
plt.scatter(x_vals, y_vals, color='red', label='Data Points')

# 计算并绘制拉格朗日函数
x_range = np.linspace(min(x_vals), max(x_vals), 100)
y_range = [lagrange(x, points) for x in x_range]
plt.plot(x_range, y_range, color='blue', label='Lagrange Polynomial')

plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Lagrange Interpolation')
plt.legend()
plt.grid(True)
plt.show()