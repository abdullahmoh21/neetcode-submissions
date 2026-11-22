from functools import cache
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def dp(i, rem):
            if rem == 0:
                return 0
                
            if i >= len(coins):
                return float('inf')

            if rem < 0:
                return float('inf')
            
            return min(1 + dp(i, rem - coins[i]), dp(i + 1, rem))
        
        coins = dp(0, amount)
        return -1 if coins == float('inf') else coins