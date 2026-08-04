class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        current_chars = set()

        i, j = 0, 0
        max_len = 1

        while j < len(s):
            if s[j] in current_chars:
                current_chars.discard(s[i])
                i += 1     
            else:
                max_len = max(max_len, (j - i) + 1)
                current_chars.add(s[j])

                j += 1       

        return max_len