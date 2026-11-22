class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            num1 = nums[i]
            j = i + 1
            k = len(nums) - 1
            while j < k:
                num2 = nums[j]
                num3 = nums[k]
                triplet_sum = num1 + num2 + num3
                if triplet_sum == 0:
                    res.append([num1, num2, num3])
                    cur = nums[j]
                    while j < k and cur == nums[j]:
                        j += 1
                    cur = nums[k] 
                    while j < k and cur == nums[k]:
                        k -= 1
                        
                elif triplet_sum < 0:
                    j += 1
                else:
                    k -= 1
        return res

                    
