class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        res = []
        for i in nums:
            if i == val:
                continue
            res.append(i)
        for v in range(len(res)):
            nums[v] = res[v]
        return len(res)