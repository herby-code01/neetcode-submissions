from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        left = 0
        mx_freq = 0

        for right in range(len(s)):
            freq[s[right]]+=1

            mx_freq = max(mx_freq, freq[s[right]])
            replacements = (right - left + 1) - mx_freq

            if replacements > k:
                freq[s[left]]-=1
                left+=1
        return right - left +1
        