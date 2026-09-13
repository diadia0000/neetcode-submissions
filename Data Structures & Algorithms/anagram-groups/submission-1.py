from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        Map = defaultdict(list)
        for i in range(len(strs)):
            char = [0]*26
            for j in strs[i]:
                char[ord(j) - ord('a')]+=1
            Map[tuple(char)].append(strs[i])
        # print(Map.values())
        return sorted(list(Map.values()))