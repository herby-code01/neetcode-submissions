class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num = set(nums)
        longest = 0

        for i in num:
            if i - 1 not in num:
                current = 1
                while i + current in num: 
                    current +=1
                longest = max(current, longest)

        return longest