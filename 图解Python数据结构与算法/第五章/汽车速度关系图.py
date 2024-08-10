import matplotlib.pyplot as plt
import numpy as np

# 生成时间数据（小时）
time = np.random.uniform(0, 5, 20)  # 生成20个随机时间数据点

# 根据线性关系生成距离数据（公里）
speed = 30  # 时速30km/h
distance = speed * time

# 绘制散点图
plt.figure(figsize=(8, 6))
plt.scatter(time, distance, color='blue')
plt.title('Scatter Plot of Time vs Distance')
plt.xlabel('Time (hours)')
plt.ylabel('Distance (kilometers)')
plt.grid(True)
plt.show()
