class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        res = set()
        mx = 0

        for right in range(len(s)):
            while s[right] in res:
                res.remove(s[left])  
                left+=1
            res.add(s[right])
            mx = max(mx, right - left +1)
        return mx      