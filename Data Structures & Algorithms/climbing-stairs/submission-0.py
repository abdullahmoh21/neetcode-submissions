from functools import cache
class Solution:
    def climbStairs(self, n: int) -> int:

        @cache
        def ways(r):
            if r == 0:
                return 1
            
            if r < 0:
                return 0
            
            return ways(r - 1) + ways(r - 2)
        
        return ways(n)
            
            
            