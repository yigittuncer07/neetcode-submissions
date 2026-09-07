class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        cache = set()

        def f(i):

            if i == len(nums) - 1:
                return True

            for j in range(1, min(nums[i] + 1, len(nums) - i)):
                if (i + j) in cache:
                    continue
                if f(i + j):
                    return True
                cache.add(i + j)
                
                
            return False
        
        return f(0)