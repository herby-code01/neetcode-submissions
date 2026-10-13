class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        array = {}
        for i in range(len(nums)):
            j = target - nums[i]
            if j in array:
                return [array[j], i]
            else:
                array[nums[i]] = i
        