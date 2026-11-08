from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        mst_freq = []

        for i in range(len(nums)):
            count[nums[i]] +=1
        b = 0
        while b < k:
            a = max(count, key=count.get)
            mst_freq.append(a)
            count.pop(a)
            b+=1
        return mst_freq



