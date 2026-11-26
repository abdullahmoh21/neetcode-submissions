class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float('-inf')
        def dfs(i, cur_sum):
            nonlocal max_sum
            
            if i == len(nums):
                return

            cur_sum = max(nums[i], cur_sum + nums[i])

            max_sum = max(max_sum, cur_sum)
            dfs(i + 1, cur_sum)

        dfs(0,0)
        return max_sum