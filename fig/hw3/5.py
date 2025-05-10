def knapsackpack(weights, values, W):
    n = len(values)
    dp = [[0] * (W + 1) for _ in range(n + 1)]

    # 填充dp数组
    for i in range(1, n + 1):
        for w in range(W + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-weights[i-1]] + values[i-1])
            else:
                dp[i][w] = dp[i-1][w]

    return dp[n][W]

# 示例
weights = [5, 4, 6, 3]
values = [10, 40, 30, 50]
W = 9
max_value = knapsackpack(weights, values, W)
print("最大价值为:", max_value)