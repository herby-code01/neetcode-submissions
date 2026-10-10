class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr = {}
        for i in range(0, len(nums)):
            h = target - nums[i]

            if h in arr:
                return [arr[h], i]
            else:
                arr[nums[i]] = i