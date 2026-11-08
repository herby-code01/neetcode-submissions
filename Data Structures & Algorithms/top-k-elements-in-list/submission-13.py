from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        mx_freq = []
        b = 0

        while b < k:
            a = max(count, key=count.get)
            mx_freq.append(a)
            count.pop(a)
            b+=1
        return mx_freq