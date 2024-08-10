def maximize_performance(n, B, cost, benefit):
    # 按照 benefit 降序排序
    sorted_projects = sorted(zip(cost, benefit), key=lambda x: x[1], reverse=True)
    sorted_cost, sorted_benefit = zip(*sorted_projects)

    dp = [[0] * (B + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for b in range(1, B + 1):
            if sorted_cost[i - 1] > b:
                dp[i][b] = dp[i - 1][b]
            else:
                dp[i][b] = max(dp[i - 1][b - sorted_cost[i - 1]] + sorted_benefit[i - 1], dp[i - 1][b])

    return dp[n][B]

# 示例数据
n = 5
B = 10
cost = [5, 3, 2, 7, 4]
benefit = [8, 5, 3, 10, 7]

result = maximize_performance(n, B, cost, benefit)
print("最大员工绩效提升:", result)
