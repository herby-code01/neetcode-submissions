
class Solution:
    def frequencySort(self, s: str) -> str:
        std = {}
        for i in s:
            if i in std:
                std[i] +=1
            else:
                std[i] = 1
        res = ""
        while std: 
            mx = max(std, key = std.get)
            res +=(mx*std[mx])
            std.pop(mx)
        return res
        