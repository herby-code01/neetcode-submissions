class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        cnt = {}
        for i in nums:
            if i in cnt:
                cnt[i] +=1
            else:
                cnt[i] = 1
        res = []

        while cnt:
            mn = min(cnt)
            if cnt[mn] > 1:
                res.extend([mn] * cnt[mn])
            else:
                res.append(mn)
            cnt.pop(mn)

        return res