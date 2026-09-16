class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        
        j = 0
        for c in t:
            if j == len(s) - 1:
                return True
            if c == s[j]:
                j += 1
        
        return False