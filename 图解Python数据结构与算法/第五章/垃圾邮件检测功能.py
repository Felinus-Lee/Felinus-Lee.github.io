import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# 示例数据集，包含邮件内容和标签（0为非垃圾邮件，1为垃圾邮件）
emails = [
    ('Get free money', 1),
    ('Claim your prize', 1),
    ('Send money now', 1),
    ('Get free gift', 1),
    ('Congratulations, you have won', 1),
    ('Meeting agenda', 0),
    ('Reminder: project deadline', 0),
    ('Lunch menu for today', 0),
    ('Meeting minutes', 0),
    ('Thank you for your email', 0)
]

# 将邮件内容和标签分离
X = [email[0] for email in emails]
y = [email[1] for email in emails]

# 将文本数据转换为特征向量
vectorizer = CountVectorizer()
X_vectorized = vectorizer.fit_transform(X)

# 划分数据集为训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X_vectorized, y, test_size=0.2, random_state=42)

# 训练逻辑回归模型
model = LogisticRegression()
model.fit(X_train, y_train)

# 在测试集上评估模型性能
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
print("Classification Report:\n", classification_report(y_test, y_pred))

# 使用训练好的模型进行预测
new_emails = [
    'Get your free gift now',
    'Important project update',
    'You have won a prize'
]
new_emails_vectorized = vectorizer.transform(new_emails)
predictions = model.predict(new_emails_vectorized)
for email, prediction in zip(new_emails, predictions):
    print("Email:", email)
    print("Prediction (1 for spam, 0 for non-spam):", prediction)
