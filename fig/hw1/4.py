def max_profit(profits):
    if not profits:
        return 0, None, None

    current_profit = max_profit = profits[0]
    buy_day = 0
    sell_day = 0
    start_day = 0

    for i in range(1, len(profits)):
        if current_profit + profits[i] > profits[i]:
            current_profit += profits[i]
        else:
            current_profit = profits[i]
            start_day = i

        if current_profit > max_profit:
            max_profit = current_profit
            buy_day = start_day
            sell_day = i

    return max_profit, buy_day + 1, sell_day + 1

profits = [3, 2, 1, -7, 5, 2, -1, 3, -1]
profit, buy_day, sell_day = max_profit(profits)
print(f"第{buy_day}天买入,第{sell_day}天卖出,最大收益为{profit}")
