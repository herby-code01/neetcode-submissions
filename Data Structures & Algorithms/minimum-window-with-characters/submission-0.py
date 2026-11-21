from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or len(t) > len(s):
            return ""
        
        need = Counter(t)
        missing = len(t)

        left = 0 
        min_len = float('inf')
        start = 0

        for right in range(len(s)):
            char  = s[right]

            if need[char] > 0:
                missing -=1

            need[char] -=1

            while missing == 0:
                if right - left +1 < min_len: 
                    min_len = right - left + 1
                    start = left 
                left_char = s[left]
                need[left_char] +=1

                if need[left_char] > 0:
                    missing +=1 
                left+=1
        if min_len == float('inf'):
            return ""
        return s[start: start + min_len]