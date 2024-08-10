import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
 
# Load data
df = pd.read_csv('.\housing.data', header=None, sep='\s+')
df.columns = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']
 
# Visualize data
cols = ['CRIM', 'RM', 'TAX', 'PTRATIO', 'MEDV']
sns.pairplot(df[cols], height=2.5)
plt.tight_layout()
plt.show()
 
# Visualize correlation matrix
cm = np.corrcoef(df[cols].values.T)
hm = sns.heatmap(cm, cbar=True, square=True, fmt='.2f', annot=True, annot_kws={'size':15}, yticklabels=cols, xticklabels=cols)
plt.show()


# Prepare data for model
X = df['RM'].values.reshape(-1, 1)
y = df['MEDV'].values
X_train,X_test,y_train,y_test = train_test_split(X, y, test_size=0.4, random_state=1)
 
# Train model
forest = RandomForestRegressor(n_estimators=1000, criterion='squared_error', random_state=1, n_jobs=-1)
forest.fit(X_train,y_train)
 
# 模型预测
y_test_pred = forest.predict(X_test)
 
# 模型性能评估
mse_test = mean_squared_error(y_test, y_test_pred)
r2_test = r2_score(y_test, y_test_pred)
print("mse_test={:.2f} r2_test={:.2f}".format(mse_test, r2_test))
 
# 绘制残差图
plt.scatter(y_test_pred, y_test_pred-y_test, c='steelblue', edgecolor='white', marker='s', s=35, alpha=0.9,label='test data')
plt.xlabel = ('Predicted values')
plt.ylabel = ('Residuals')
plt.legend(loc='upper left')
plt.hlines(y=0, xmin=-10, xmax=50, lw=2, color='black')
plt.xlim([10,48])
plt.tight_layout()
plt.show()
