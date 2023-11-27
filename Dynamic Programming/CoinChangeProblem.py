# Lecture method of implementing coin change problem - 1D array

def coinChange(coins, amount):
    dp = [float('inf') for _ in range(amount + 1)]
    dp[0] = 0
    coin_used = [-1 for _ in range(amount + 1)]

    for coin in coins:
        for i in range(coin, amount+1):  # iterating through all possible changes till amount
            if dp[i-coin] != float('inf'):
                dp[i] = min(dp[i], dp[i-coin] + 1)
                if dp[i] == dp[i-coin] + 1:
                    coin_used[i] = coin

    return dp, dp[amount], coin_used


if __name__ == '__main__':
    coins = [7, 2, 3, 6]
    total = 13
    dp_val, no_coins, coins_used = coinChange(coins, total)
    change_coins = []
    amount = total
    while amount > 0:
        coin = coins_used[amount]
        change_coins.append(coin)
        amount -= coin

    print("No of coins used = ", no_coins)
    print("Coin denominations used are: ", change_coins)
    print(coins_used)
