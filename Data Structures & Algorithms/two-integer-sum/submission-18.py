class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = {}

        for i in range(len(nums)):
            j = target - nums[i]

            if j in s:
                return [s[j], i]
            else:
                s[nums[i]] = i