from functools import cache
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * (n + 2)
        for i in range(n - 1, -1, -1):
            dp[i] = cost[i] + min(dp[i + 1], dp[i + 2])
        return min(dp[0], dp[1])

            
        # @cache
        # def dp(i):
        #     if i >= len(cost):
        #         return 0
            
        #     return cost[i] + min(dp(i + 1), dp(i + 2))
        
        # return min(dp(0), dp(1))