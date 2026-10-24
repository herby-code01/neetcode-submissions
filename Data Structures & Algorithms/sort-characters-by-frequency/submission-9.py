from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        return ''.join(sorted(s, key=lambda x: (-count[x], x)))
        