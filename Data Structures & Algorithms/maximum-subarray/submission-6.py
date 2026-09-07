class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum = 0
        ans = float('-inf')

        i = 0
        for j, n in enumerate(nums):

            cur_sum = max(cur_sum, 0)

            cur_sum += n
            ans = max(ans, cur_sum)
            
        return ans

