import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# 生成随机数据点
np.random.seed(0)
x = np.sort(np.random.uniform(0, 10, 10))
y = np.sin(x)

# 样条插值
def spline_interpolation(x, y, xi):
    spline = interp1d(x, y, kind='cubic')
    return spline(xi)

# 生成插值点
xi = np.linspace(min(x), max(x), 1000)

# 计算插值结果
yi_spline = spline_interpolation(x, y, xi)

# 绘图
plt.figure(figsize=(10, 6))
plt.scatter(x, y, label='Data Points')
plt.plot(xi, yi_spline, label='Spline Interpolation', color='blue')
plt.title('Spline Interpolation')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()
