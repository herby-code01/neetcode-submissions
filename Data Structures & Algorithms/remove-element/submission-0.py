class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        res = []
        for i in nums:
            if i == val:
                continue
            res.append(i)
        k = len(res)
        for v in range(k):
            nums[v] = res[v]
        return k