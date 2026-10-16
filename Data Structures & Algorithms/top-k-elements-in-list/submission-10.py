from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        result = []
        for _ in range(k):
            m = max(count, key=count.get)
            result.append(m)
            del count[m]
        return result