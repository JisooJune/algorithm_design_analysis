def subset_sum(S, W):
    n = len(S)
    # 初始化dp数组
    dp = [[False] * (W + 1) for _ in range(n + 1)]
    # 空集的和为0
    for i in range(n + 1):
        dp[i][0] = True

    # 填充dp数组
    for i in range(1, n + 1):
        for j in range(1, W + 1):
            if S[i-1] <= j:
                dp[i][j] = dp[i-1][j] or dp[i-1][j - S[i-1]]
            else:
                dp[i][j] = dp[i-1][j]

    return dp[n][W]

# 示例
S = [1, 4, 7, 3, 5]
W = 11
result = subset_sum(S, W)
print("输出:", result)  # 输出: True