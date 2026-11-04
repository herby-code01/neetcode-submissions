class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        res = set()
        mx = 0

        for r in range(len(s)):
            while s[r] in res:
                res.remove(s[l])
                l+=1
            res.add(s[r])
            mx = max(mx, r - l+1)

        return mx
        
        