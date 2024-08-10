def build_adj_matrix(array):
    n = len(array)
    adj_matrix = [[0] * n for _ in range(n)]

    for i in range(n):
        left_child = 2 * i + 1
        right_child = 2 * i + 2

        if left_child < n:
            adj_matrix[i][left_child] = 1
            adj_matrix[left_child][i] = 1

        if right_child < n:
            adj_matrix[i][right_child] = 1
            adj_matrix[right_child][i] = 1

    return adj_matrix

# 给定的数组
array = [2, 6, 8, 5, 3, 7, 1, 4]

# 构建邻接矩阵
adj_matrix = build_adj_matrix(array)

# 输出邻接矩阵
print("邻接矩阵：")
for row in adj_matrix:
    print(row)
