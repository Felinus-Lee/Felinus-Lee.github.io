import numpy as np

# 定义无向图的顶点和边
V = {1, 2, 3, 4}
E = {(1, 2), (1, 3), (2, 4)}

# 初始化邻接矩阵
n = len(V)
adj_matrix = np.zeros((n, n), dtype=int)

# 填充邻接矩阵
for edge in E:
    u, v = edge
    adj_matrix[u-1][v-1] = 1
    adj_matrix[v-1][u-1] = 1  # 因为是无向图

print("无向图的邻接矩阵：")
print(adj_matrix)
