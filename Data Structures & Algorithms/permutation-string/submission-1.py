class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target_count = defaultdict(int)
        count = defaultdict(int)
        
        for c in s1:
            target_count[c] += 1
        
        i = 0
        for j in range(len(s2)):
            if s2[j] not in target_count:
                i = j + 1
                count = defaultdict(int)

            else:
                count[s2[j]] += 1
                while count[s2[j]] > target_count[s2[j]]:
                    count[s2[i]] -= 1
                    i += 1
                
                if j - i + 1 == len(s1):
                    return True
        return False