class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_max = nums[0]
        cur_min = nums[0]
        ans = nums[0]

        for num in nums[1:]:
            candidates = (
                num,
                cur_max * num,
                cur_min * num
            )

            cur_max = max(candidates)
            cur_min = min(candidates)

            ans = max(ans, cur_max)

        return ans







        # @cache
        # def dp(i, j, cur_product):
        #     if j >= len(nums) or i>= len(nums):
        #         return cur_product

        #     print(f"for ({i},{j})= {cur_product}")
        #     return max(
        #         cur_product,
        #         dp(i, j + 1, cur_product * nums[j]),
        #         dp(i + 1, i + 2,  nums[i + 1])
        #     )

        # return dp(0, 1, nums[0])