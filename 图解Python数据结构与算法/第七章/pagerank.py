import numpy as np

# 定义网页链接矩阵
# 行表示来源网页，列表示目标网页
link_matrix = np.array([
    [0, 1, 0, 1],  # A -> B, D
    [0, 0, 1, 0],  # B -> C
    [1, 0, 0, 0],  # C -> A
    [0, 0, 1, 0]   # D -> C
])

# 初始化PageRank值
n = link_matrix.shape[0]
pagerank = np.ones(n) / n

# 设置阻尼因子
damping_factor = 0.85

# 开始迭代计算PageRank
def calculate_pagerank(link_matrix, pagerank, damping_factor, iterations=100):
    for i in range(iterations):
        new_pagerank = np.ones(n) * (1 - damping_factor) / n
        for j in range(n):
            for k in range(n):
                if link_matrix[k, j] == 1:
                    out_degree = np.sum(link_matrix[k])
                    new_pagerank[j] += damping_factor * pagerank[k] / out_degree
        pagerank = new_pagerank
    return pagerank

pagerank = calculate_pagerank(link_matrix, pagerank, damping_factor)
print("PageRank值:", pagerank)
