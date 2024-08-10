from sklearn.tree import DecisionTreeClassifier

# 创建样本数据
X = [[0, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]]#0表示阴天、28度以上、紫外线强度大于等于3
y = [0, 0, 0, 1]  # 0表示不适合野餐，1表示适合野餐

# 创建决策树模型
clf = DecisionTreeClassifier(random_state=42)

# 拟合模型
clf.fit(X, y)

# 输入新的天气、温度和紫外线条件
new_data = [[1, 1, 1]]  # 例如：天气是晴天、温度不超过28度、紫外线强度大于等于3

# 进行预测
prediction = clf.predict(new_data)

# 根据预测结果输出判断
if prediction[0] == 1:
    print("适合野餐！")
else:
    print("不适合野餐！")
