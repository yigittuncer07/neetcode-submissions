class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = defaultdict(int)
        ans = 0
        i = 0
        maxf = 0
        for j in range(len(s)):
            counts[s[j]] += 1
            maxf = max(maxf, counts[s[j]])

            while ((1 + j - i) - maxf) > k:
                counts[s[i]] -= 1
                i += 1

            ans = max(ans, 1 + j - i)

        return ans

