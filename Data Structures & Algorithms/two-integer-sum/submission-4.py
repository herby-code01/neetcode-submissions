class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i in range(0, len(nums)):
            h = target - nums[i]
            if h in nums[i+1:]:
                return [i, nums.index(h, i + 1)]