import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# 生成模拟数据
np.random.seed(0)
X = np.sort(5 * np.random.rand(200, 1), axis=0)
y = np.sin(X).ravel() + np.random.normal(0, 0.1, X.shape[0])

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 使用多项式特征转换器将特征转换成多项式特征
degree = 3  # 设置多项式的阶数
poly_features = PolynomialFeatures(degree=degree)
X_train_poly = poly_features.fit_transform(X_train)
X_test_poly = poly_features.transform(X_test)

# 训练线性回归模型
model = LinearRegression()
model.fit(X_train_poly, y_train)

# 在训练集和测试集上评估模型
y_train_pred = model.predict(X_train_poly)
train_rmse = np.sqrt(mean_squared_error(y_train, y_train_pred))

y_test_pred = model.predict(X_test_poly)
test_rmse = np.sqrt(mean_squared_error(y_test, y_test_pred))

print(f"训练集 RMSE: {train_rmse}")
print(f"测试集 RMSE: {test_rmse}")

# 可视化拟合结果
plt.scatter(X, y, color='blue', label='Original data')
plt.plot(X, model.predict(poly_features.transform(X)), color='red', label='Fitted line')
plt.title('Polynomial Regression')
plt.xlabel('X')
plt.ylabel('y')
plt.legend()
plt.show()
