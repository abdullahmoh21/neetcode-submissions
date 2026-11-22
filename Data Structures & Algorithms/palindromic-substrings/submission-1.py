class Solution:
    def countSubstrings(self, s: str) -> int:
        def expand(l, r):
            res = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
            return res
                    
        count = 0
        for c in range(len(s)):
            count += expand(c, c)
            count += expand(c, c+1)
        return count