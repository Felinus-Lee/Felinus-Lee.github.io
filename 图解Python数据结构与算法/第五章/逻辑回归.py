import numpy as np
import matplotlib.pyplot as plt

# Sigmoid 函数
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# 生成一些示例数据
np.random.seed(0)
X = np.random.randn(100, 2)
y = np.random.randint(0, 2, size=100)

# 训练逻辑回归模型
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(X, y)

# 提取模型参数
theta_0 = model.intercept_[0]
theta_1, theta_2 = model.coef_[0]

# 将数据分为两个类别
class_0 = X[y == 0]
class_1 = X[y == 1]

# 绘制原始数据的散点图
plt.figure(figsize=(12, 4))
plt.subplot(1, 3, 1)
plt.scatter(class_0[:, 0], class_0[:, 1], color='blue', label='Class 0')
plt.scatter(class_1[:, 0], class_1[:, 1], color='red', label='Class 1')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.title('Original Data')
plt.legend()

# 绘制拟合到 sigmoid 函数的图
plt.subplot(1, 3, 2)
plt.scatter(class_0[:, 0], class_0[:, 1], color='blue', label='Class 0')
plt.scatter(class_1[:, 0], class_1[:, 1], color='red', label='Class 1')

# 计算拟合直线的斜率和截距
x_values = np.linspace(-3, 3, 100)
y_values = -(theta_1 * x_values + theta_0) / theta_2

# 使用 sigmoid 函数将拟合直线限制在0和1之间
y_values = sigmoid(y_values)

plt.plot(x_values, y_values, color='green', label='Decision Boundary')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.title('Logistic Regression Fit')
plt.legend()

# 绘制预测图
plt.subplot(1, 3, 3)
plt.scatter(class_0[:, 0], class_0[:, 1], color='blue', label='Class 0')
plt.scatter(class_1[:, 0], class_1[:, 1], color='red', label='Class 1')

# 新的测试数据点
x_new = np.array([[0, 1]])  
y_new = model.predict(x_new)
plt.scatter(x_new[:, 0], x_new[:, 1], color='green', marker='x', label='New Prediction: Class {}'.format(y_new[0]))

plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.title('Prediction')
plt.legend()

plt.tight_layout()
plt.show()
