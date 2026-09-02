import random
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k

        left, right = 0, len(nums) - 1

        while left <= right:

            pivot = right
            p = left
            i = left
            while i < right:
                if nums[i] < nums[pivot]:
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1
                i += 1

            nums[i], nums[p] = nums[p], nums[i]

            if k == p:
                return nums[p]
            elif k < p:
                right = p - 1
            else:
                left = p + 1
        




    
    # def findKthLargest(self, nums: List[int], k: int) -> int:
    #     min_heap = []

    #     for num in nums:
    #         if len(min_heap) < k:
    #             heapq.heappush(min_heap, num)
    #         elif min_heap[0] < num:
    #             heapq.heapreplace(min_heap, num)
        
    #     return min_heap[0]
    
    # def findKthLargest(self, nums: List[int], k: int) -> int:
        