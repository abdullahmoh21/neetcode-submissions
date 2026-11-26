from functools import cache
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        @cache
        def dfs(i):
            if i >= len(nums):
                return False

            if i == len(nums) - 1:
                return True
            
            for di in range(nums[i], 0, -1):
                ni = i + di

                if ni >= len(nums):
                    continue

                if dfs(ni):
                    return True

            return False

        return dfs(0)

            