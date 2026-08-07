class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = defaultdict(int)
        ans = 0
        i = 0
        for j in range(len(s)):
            counts[s[j]] += 1

            while ((1 + j - i) - max(counts.values())) > k:
                counts[s[i]] -= 1
                i += 1

            ans = max(ans, 1 + j - i)

        return ans

