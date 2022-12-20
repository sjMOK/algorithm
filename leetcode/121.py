def max_profit(prices):
    max_profit = 0
    i = 0
    while i < len(prices) - 1:
        if prices[i] < prices[i + 1]:   # find increasing point
            max_price = max(prices[i:])
            max_price_idx = i + prices[i:].index(max_price)
            sub_prices = prices[i:max_price_idx + 1]

            min_price = min(sub_prices)
            profit = max_price - min_price
            max_profit = max(max_profit, profit)

            i = max_price_idx

        i += 1

    return max_profit
