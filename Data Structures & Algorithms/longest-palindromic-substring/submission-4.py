from functools import cache
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(i, j):
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
            return i + 1, j - 1

        best = (0, 0)
        for c in range(len(s)):
            for i, j in (expand(c, c), expand(c, c + 1)):
                if j - i > best[1] - best[0]:
                    best = (i, j)
        return s[best[0]:best[1] + 1]

        # THIS IS SHITTY CAUSE WE LOOP FROM OUT IN SO NO DEPENDENCIES ARE CACHED
        # @cache
        # def isPalindrom(i, j):
        #     if i > j:
        #         return True
            
        #     if s[i] == s[j]:
        #         return isPalindrom(i+1, j-1)
            
        #     return False

        # if len(s) == 1:
        #     return s


        # max_ = (0, 0)
        # for i in range(len(s)):
        #     for j in range(i, len(s)):
        #         if j - i > max_[1] - max_[0] and isPalindrom(i, j):
        #             max_ = (i, j)
        # return s[max_[0]: max_[1] + 1]




