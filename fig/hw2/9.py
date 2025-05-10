def two_knapsack(V, W, c):
    n = len(V)
    dp = [[[0 for _ in range(c + 1)] for _ in range(c + 1)] for _ in range(n + 1)]

    trace = [[[0 for _ in range(c + 1)] for _ in range(c + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(c + 1):
            for k in range(c + 1):
                # 不放入背包
                dp[i][j][k] = dp[i - 1][j][k]
                trace[i][j][k] = 0

                # 放入第一个背包
                if j >= W[i - 1] and dp[i - 1][j - W[i - 1]][k] + V[i - 1] > dp[i][j][k]:
                    dp[i][j][k] = dp[i - 1][j - W[i - 1]][k] + V[i - 1]
                    trace[i][j][k] = 1

                # 放入第二个背包
                if k >= W[i - 1] and dp[i - 1][j][k - W[i - 1]] + V[i - 1] > dp[i][j][k]:
                    dp[i][j][k] = dp[i - 1][j][k - W[i - 1]] + V[i - 1]
                    trace[i][j][k] = 2

    # 回溯找到具体物品
    max_value = dp[n][c][c]
    bag1 = []
    bag2 = []
    i = n
    j = c
    k = c

    while i > 0:
        if trace[i][j][k] == 1:
            bag1.append(i)
            j -= W[i - 1]
        elif trace[i][j][k] == 2:
            bag2.append(i)
            k -= W[i - 1]
        i -= 1

    return max_value, bag1, bag2


v = [1, 3, 2, 5, 8, 7]
w = [1, 3, 2, 5, 8, 7]
c = 7

max_value, bag1, bag2 = two_knapsack(v, w, c)

print(f"最大价值为{max_value}, 背包装的物品为：{bag1} {bag2}")
# 输出: 最大价值= 14
# 背包1的物品为: [6]
# 背包2的物品为 [4, 3]