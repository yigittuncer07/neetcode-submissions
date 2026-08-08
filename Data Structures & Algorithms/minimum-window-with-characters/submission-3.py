class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target_count = defaultdict(int)
        count = defaultdict(int)
        for c in t:
            target_count[c] += 1


        i = 0
        min_len, ans = float('inf'), (0,0)
        need, have = len(target_count), 0

        for j in range(len(s)):
            if s[j] not in target_count:
                continue
            
            count[s[j]] += 1
            if count[s[j]] == target_count[s[j]]:
                have += 1
            
            while need == have:
                if j - i + 1 < min_len:
                    min_len = j - i + 1
                    ans = (i,j)
                
                if s[i] in count:
                    count[s[i]] -= 1
                    if count[s[i]] < target_count[s[i]]:
                        have -= 1
                    
                i += 1
        return s[ans[0]:ans[1] + 1] if min_len < float('inf') else ''




