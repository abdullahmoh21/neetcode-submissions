class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        min_price = float('inf')
        for p in prices:
            min_price = min(min_price, p)
            best = max(best, p - min_price)
        return best