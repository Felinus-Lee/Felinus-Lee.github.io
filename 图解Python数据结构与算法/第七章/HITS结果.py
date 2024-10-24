import numpy as np

# 定义网页链接结构的邻接矩阵
# 0 -> A, 1 -> B, 2 -> C, 3 -> D, 4 -> E
# A -> B, C
# B -> D
# C -> D
# D -> A, B, C
# E -> A, B, C
links = np.array([
    [0, 1, 1, 0, 0],  # A -> B, C
    [0, 0, 0, 1, 0],  # B -> D
    [0, 0, 0, 1, 0],  # C -> D
    [1, 1, 1, 0, 0],  # D -> A, B, C
    [1, 1, 1, 0, 0]   # E -> A, B, C
])

# 初始化Hub和Authority值
n = links.shape[0]
hub_scores = np.ones(n)
auth_scores = np.ones(n)

# 迭代次数
iterations = 10

for _ in range(iterations):
    # 更新Authority值
    auth_scores = np.dot(links.T, hub_scores)
    
    # 更新Hub值
    hub_scores = np.dot(links, auth_scores)
    
    # 归一化处理
    auth_scores = auth_scores / np.linalg.norm(auth_scores)
    hub_scores = hub_scores / np.linalg.norm(hub_scores)

# 输出最终的Hub和Authority值
print("最终的Hub值:", hub_scores)
print("最终的Authority值:", auth_scores)
