def max_profit_optimized(budget, weights, rates):
    n = len(weights)
    dp = [0] * (budget + 1)

    for i in range(1, n + 1):
        for j in range(budget, 0, -1):
            if weights[i - 1] <= j:
                dp[j] = max(dp[j], dp[j - weights[i - 1]] + rates[i - 1] * weights[i - 1])

    return max(dp)


weights = [5000, 3000, 2000]  # 投资金额
rates = [0.1, 0.08, 0.12]  # 预期收益率
budget = 10000  # 预算
max_profit_value = max_profit_optimized(budget, weights, rates)
print("最大收益为:", max_profit_value)