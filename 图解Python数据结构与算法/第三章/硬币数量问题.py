def min_coins(amount):
    coins = [1, 2, 5]
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount]

amount_to_pay = 13
result = min_coins(amount_to_pay)