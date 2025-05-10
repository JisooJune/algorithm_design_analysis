def min_edit_distance(x, y):
    n = len(x)
    m = len(y)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # 初始化
    for i in range(n + 1):
        dp[i][0] = i
    for j in range(m + 1):
        dp[0][j] = j

    # 填充dp数组
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if x[i - 1] == y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j] + 1,      # 删除
                                 dp[i][j - 1] + 1,      # 插入
                                 dp[i - 1][j - 1] + 1)  # 替换

    return dp[n][m]

# 示例
x = "abcd"
y = "bcfe"
result = min_edit_distance(x, y)
print("最少操作数:", result)  # 输出: 3