import numpy as np

# 定义网页链接矩阵 (每行表示来源网页，列表示目标网页)
link_matrix = np.array([
    [0, 1, 1, 0, 0],  # A -> B, C
    [0, 0, 1, 1, 0],  # B -> C, D
    [1, 0, 0, 1, 0],  # C -> A, D
    [0, 0, 1, 0, 1],  # D -> C, E
    [1, 0, 0, 0, 0]   # E -> A
])

# 定义点击率（人为定义的访问概率）
click_rates = np.array([0.20, 0.25, 0.15, 0.30, 0.10])

# 初始化PageRank值
n = link_matrix.shape[0]
pagerank = np.ones(n) / n

# 设置阻尼因子
damping_factor = 0.85

# 开始迭代计算PageRank
def calculate_pagerank(link_matrix, click_rates, pagerank, damping_factor, iterations=100):
    for i in range(iterations):
        new_pagerank = (1 - damping_factor) * click_rates  # 引入点击率
        for j in range(n):
            for k in range(n):
                if link_matrix[k, j] == 1:
                    out_degree = np.sum(link_matrix[k])
                    new_pagerank[j] += damping_factor * pagerank[k] / out_degree
        pagerank = new_pagerank
    return pagerank

pagerank = calculate_pagerank(link_matrix, click_rates, pagerank, damping_factor)
print("考虑点击率、引用量和质量的PageRank值:", pagerank)
