from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        count = Counter(nums)

        for _ in range(k):
            mx = max(count, key=count.get)
            result.append(mx)
            del count[mx]
        
        return result
        