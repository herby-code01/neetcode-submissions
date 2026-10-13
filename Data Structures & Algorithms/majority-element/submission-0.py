class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        val = {}
        count = 0
        for i in range(len(nums)):
            if nums[i] in val:
                count+=1
                val[nums[i]]= count
            else:
                count = 1
                val[nums[i]]= count
        return max(val, key=val.get)