from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        res = ""
        while count:
            mx = max(count, key=count.get)
            res+=(mx*count[mx])
            count.pop(mx)
        return res        