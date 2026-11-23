from functools import cache
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def dp(i, rem):
            if i == len(coins):
                return float('inf')
            
            if rem < 0:
                return float('inf')
            
            if rem == 0:
                return 0

            return min(1 + dp(i, rem - coins[i]), dp(i + 1, rem))

        return -1 if (ans := dp(0, amount)) == float('inf') else ans