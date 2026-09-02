import random
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        target_idx = len(nums) - k
        left, right = 0, len(nums) - 1
        
        while left <= right:
            # Randomize pivot to avoid O(N^2) time complexity on sorted arrays
            pivot_idx = random.randint(left, right)
            nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]
            
            pivot = nums[right]
            p = left
            
            # Partition the sub-array
            for i in range(left, right):
                if nums[i] < pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            
            # Move pivot to its final place
            nums[p], nums[right] = nums[right], nums[p]
            
            # Narrow the search space
            if p == target_idx:
                return nums[p]
            elif p < target_idx:
                left = p + 1
            else:
                right = p - 1




    
    # def findKthLargest(self, nums: List[int], k: int) -> int:
    #     min_heap = []

    #     for num in nums:
    #         if len(min_heap) < k:
    #             heapq.heappush(min_heap, num)
    #         elif min_heap[0] < num:
    #             heapq.heapreplace(min_heap, num)
        
    #     return min_heap[0]
    
    # def findKthLargest(self, nums: List[int], k: int) -> int:
        