class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_Map = {}
        t_Map = {}
        for i in s:
            if i not in s_Map:
                s_Map[i] = 0
            s_Map[i]+=1
        for i in t:
            if i not in t_Map:
                t_Map[i] = 0
            t_Map[i]+=1
        return s_Map == t_Map
