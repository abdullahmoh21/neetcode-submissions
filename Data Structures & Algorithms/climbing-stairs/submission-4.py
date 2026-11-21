from functools import cache
class Solution:
    def climbStairs(self, n: int) -> int:
        ways = [0] * (n+1)
        ways[0] = 1
        for i in range(len(ways)):
            if i + 1 < len(ways):
                ways[i + 1] += ways[i]
            if i + 2 < len(ways):
                ways[i + 2] += ways[i]
        return ways[-1]
        # @cache
        # def ways(n):
        #     if n == 0:
        #         return 1
     
        #     if n < 0:
        #         return 0
            
        #     return ways(n-1) + ways(n-2)
        # return ways(n)