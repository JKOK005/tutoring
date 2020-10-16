def getWays(amount, coins):
	dp = [1] + [0]*amount
	for coin in coins:
		for i in range(coin, amount+1):
			dp[i] += dp[i-coin]
		print(dp)
	return dp[amount]