class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        ans = max(piles)
        i = 1
        j = max(piles) - 1

        while i <= j:
            k = (i + j) // 2

            hours = 0
            for val in piles:
                hours += -(-val // k)
            
            if hours <= h:
                ans = min(ans, k)
                j = k - 1
            else:
                print(hours, h)
                i = k + 1
        return ans

            