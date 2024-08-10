import matplotlib.pyplot as plt
import numpy as np

# 生成时间数据（小时）
time = np.random.uniform(0, 5, 20)  # 生成20个随机时间数据点

# 根据线性关系生成距离数据（公里）
speed = 30  # 时速30km/h
distance = speed * time

# 进行线性拟合
fit = np.polyfit(time, distance, 1)
slope = fit[0]  # 斜率
intercept = fit[1]  # 截距

# 输出拟合直线的公式
print("拟合直线公式：y = {:.2f}x + {:.2f}".format(slope, intercept))

# 计算拟合直线上的点
fit_line_x = np.linspace(min(time), max(time), 100)
fit_line_y = slope * fit_line_x + intercept

# 绘制散点图和拟合直线
plt.figure(figsize=(8, 6))
plt.scatter(time, distance, color='blue', label='Data')
plt.plot(fit_line_x, fit_line_y, color='red', label='Linear Fit')
plt.title('Scatter Plot of Time vs Distance with Linear Fit')
plt.xlabel('Time (hours)')
plt.ylabel('Distance (kilometers)')
plt.legend()
plt.grid(True)
plt.show()
