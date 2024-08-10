import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# 定义 Gompertz 生长模型
def gompertz_growth(x, K, r, t):
    return K * np.exp(-np.exp(-r * (x - t)))

# 生成模拟数据
np.random.seed(0)
x_data = np.linspace(0, 10, 100)
y_true = 100 * np.exp(-np.exp(-0.5 * (x_data - 5)))  # 真实的生长曲线
y_data = y_true + np.random.normal(0, 5, size=len(x_data))  # 加入噪声的观测数据

# 利用 curve_fit 进行拟合
popt, pcov = curve_fit(gompertz_growth, x_data, y_data, p0=[100, 0.1, 5])

# 提取拟合的参数
K_fit, r_fit, t_fit = popt

# 绘制拟合结果
plt.scatter(x_data, y_data, label='Observations')
plt.plot(x_data, y_true, color='red', label='True Growth Curve')
plt.plot(x_data, gompertz_growth(x_data, *popt), color='green', label='Fitted Growth Curve')
plt.title('Gompertz Growth Curve Fitting')
plt.xlabel('Time')
plt.ylabel('Population')
plt.legend()
plt.show()

print("拟合参数:")
print(f"K = {K_fit:.2f}")
print(f"r = {r_fit:.2f}")
print(f"t = {t_fit:.2f}")
