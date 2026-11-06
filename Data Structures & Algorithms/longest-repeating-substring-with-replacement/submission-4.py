from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = Counter()
        mx_freq = 0
        left = 0

        for right in range(len(s)):
            freq[s[right]]+=1

            mx_freq = max(mx_freq, freq[s[right]])
            replacement = (right-left+1) - mx_freq

            if replacement > k:
                freq[s[left]] -=1
                left+=1
            
        return right-left+1





