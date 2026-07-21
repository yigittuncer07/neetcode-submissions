class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped_hm = {}
        

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord('a')] += 1
            
            count = str(count)
            if count in grouped_hm:
                grouped_hm[count].append(s)
            else:
                grouped_hm[count] = [s]
        
        return list(grouped_hm.values())