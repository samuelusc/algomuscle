class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # deploy DP to solve it 
        dp = [[0] * 4 for _ in range(len(prices))] 
        dp[0][0] = -prices[0] # first transaction
        dp[0][1] = 0
        dp[0][2] = -prices[0] # second transaction
        dp[0][3] = 0
        for i in range(1,len(prices)):
            # define four states 
            dp[i][0] = max(dp[i-1][0], -prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] + prices[i])
            dp[i][2] = max(dp[i-1][2], dp[i-1][1] - prices[i])
            dp[i][3] = max(dp[i-1][3],dp[i-1][2] + prices[i])

        return dp[-1][3]