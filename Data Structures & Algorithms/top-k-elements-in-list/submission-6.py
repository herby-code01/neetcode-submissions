from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        result = []
        for _ in range(k):
            mx_key = max(count, key=count.get)
            result.append(mx_key)
            del count[mx_key]
        return result
