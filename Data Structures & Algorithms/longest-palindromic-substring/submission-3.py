from functools import cache
class Solution:
    def longestPalindrome(self, s: str) -> str:
        @cache
        def isPalindrom(i, j):
            if i > j:
                return True
            
            if s[i] == s[j]:
                return isPalindrom(i+1, j-1)
            
            return False

        if len(s) == 1:
            return s


        max_ = (0, 0)
        for i in range(len(s)):
            for j in range(i, len(s)):
                if j - i > max_[1] - max_[0] and isPalindrom(i, j):
                    max_ = (i, j)
        return s[max_[0]: max_[1] + 1]




