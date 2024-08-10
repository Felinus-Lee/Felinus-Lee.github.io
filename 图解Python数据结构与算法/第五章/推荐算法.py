import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# 示例数据
search_histories = ["laptop", "gaming", "16GB RAM"]
product_descriptions = [
    "gaming laptop with 16GB RAM",
    "office laptop with 8GB RAM",
    "gaming desktop with 32GB RAM",
    "ultrabook with 8GB RAM",
    "laptop with 16GB RAM and 1TB SSD"
]
search_times = np.array([120, 80, 150])  # 用户在搜索结果页面的停留时间（秒）
browse_times = np.array([200, 180, 220])  # 用户在浏览商品页面的停留时间（秒）

# TF-IDF特征提取
tfidf_vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf_vectorizer.fit_transform(product_descriptions)

# 计算用户搜索历史的TF-IDF向量
user_search_vector = tfidf_vectorizer.transform(search_histories)

# 计算商品之间的余弦相似度
cosine_similarities = linear_kernel(user_search_vector, tfidf_matrix)

# 计算推荐分数
search_weight = 0.4
browse_weight = 0.6

# 计算综合推荐分数
# 假设搜索分数和浏览分数加权平均
combined_scores = (cosine_similarities.max(axis=0) * search_weight +
                   np.mean(browse_times) * browse_weight)  # 使用浏览时间的均值作为浏览分数

# 输出推荐分数最高的商品
recommended_indices = np.argsort(combined_scores)[::-1]
recommended_products = [product_descriptions[i] for i in recommended_indices]

print("推荐商品：")
for idx, product in enumerate(recommended_products):
    print(f"{idx + 1}. {product} (综合分数: {combined_scores[recommended_indices[idx]]:.2f})")
