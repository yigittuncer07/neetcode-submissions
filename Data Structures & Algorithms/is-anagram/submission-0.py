class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_set = dict()
        t_set = dict()

        for c in s:
            if s_set.get(c):
                s_set[c] += 1
            else:
                s_set[c] = 1
        
        for c in t:
            if t_set.get(c):
                t_set[c] += 1
            else:
                t_set[c] = 1

        return s_set == t_set