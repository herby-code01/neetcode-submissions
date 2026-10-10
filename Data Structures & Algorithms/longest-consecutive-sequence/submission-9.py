class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # if not nums:
        #     return 0
        # num = list(sorted(set(nums)))
        # current = 1
        # longest = 1

        # for i in range(1, len(num)):
        #     if num[i] - num[i-1] == 1:
        #         current +=1
        #     else: 
        #         current = 1
        #     longest = max(current, longest)
        # return longest
       
        num = set(nums)
        longest = 0

        for i in num:
            if i - 1 not in num:
                current = 1
                while i + current in num:
                    current += 1

                longest = max(longest, current)

        return longest
