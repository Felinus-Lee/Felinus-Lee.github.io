import numpy as np
import matplotlib.pyplot as plt

# 计算差商
def divided_difference(x, y):
    n = len(x)
    F = np.zeros((n, n))
    F[:,0] = y
    for j in range(1, n):
        for i in range(j, n):
            F[i, j] = (F[i, j-1] - F[i-1, j-1]) / (x[i] - x[i-j])
    return F

# 计算插值多项式
def newton_interpolation(x, y, xi):
    n = len(x)
    F = divided_difference(x, y)
    yi = np.zeros(len(xi))
    for i in range(n):
        term = F[i,i]
        for j in range(i):
            term *= (xi - x[j])
        yi += term
    return yi

# 生成随机数据点
np.random.seed(0)
x = np.sort(np.random.uniform(0, 10, 10))
y = np.sin(x)

# 生成插值点
xi = np.linspace(0, 10, 1000)

# 计算插值结果
yi_newton = newton_interpolation(x, y, xi)

# 绘图
plt.figure(figsize=(10, 6))
plt.scatter(x, y, label='Data Points')
plt.plot(xi, yi_newton, label='Newton Interpolation', color='red')
plt.title('Newton Interpolation')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()
