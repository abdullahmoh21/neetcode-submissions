from functools import cache

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def rob_line(line):
            print(f"got line: {line}")
            @cache
            def dp(i):
                if i >= len(line):
                    return 0
                return max(line[i] + dp(i + 2), dp(i + 1))
            return dp(0)

        return max(rob_line(nums[:-1]), rob_line(nums[1:]))
