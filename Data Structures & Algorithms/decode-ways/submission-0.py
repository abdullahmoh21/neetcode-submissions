from functools import cache
class Solution:
    def numDecodings(self, s: str) -> int:
        @cache
        def dp(i):
            if i > len(s):
                return 0

            if i == len(s):
                return 1
            
            take_one = 0
            if s[i] != "0":
                take_one = dp(i + 1)
            
            take_two = 0
            if i < len(s) - 1 and 10 <= int(s[i:i + 2]) <= 26:
                take_two = dp(i + 2)
            
            return take_one + take_two
        
        return dp(0) 

            
        