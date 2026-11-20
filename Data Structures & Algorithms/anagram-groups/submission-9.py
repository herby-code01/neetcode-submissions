from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)

        for i in strs:
            sort = tuple(sorted(i))
            group[sort].append(i)

        return list(group.values())
            