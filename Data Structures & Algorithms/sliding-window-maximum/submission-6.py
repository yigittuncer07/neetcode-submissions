class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deck = collections.deque()

        i = 0
        ans = []

        for j, c in enumerate(nums):
            if j - i == k:
                if deck[0] == nums[i]:
                    deck.popleft()
                i += 1

            if not deck:
                deck.appendleft(c)
            elif c > deck[0]:
                deck.clear()
                deck.appendleft(c)
            else:
                while c > deck[-1]:
                    deck.pop()
                deck.append(c)
                
            if j >= k - 1:
                ans.append(deck[0])

        return ans


                 

        