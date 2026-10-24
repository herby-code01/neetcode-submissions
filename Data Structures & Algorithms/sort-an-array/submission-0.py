class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return sorted(nums)
    #   left = 0
    #   right = len(nums)-1
    #   while left < right:
    #     if nums[left] > nums[right]:
    #         a = nums[left]
    #         nums[left] = nums[right]
    #     if nums[left] == nums[right]:
    #         a = nums[left]
    #         continue
    #     if nums[left] < nums[right]:
    #         a = nums[right]
    #         continue
    #     if a <= nums[left]:
    #         nums[left] = a
    #         a = nums[left]
    #     left+=1
    #     right-=1
    #   return nums
    

        