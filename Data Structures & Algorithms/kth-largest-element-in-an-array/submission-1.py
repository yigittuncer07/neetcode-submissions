class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = []
        for n in nums:
            if len(max_heap) < len(nums) - k + 1:
                heapq.heappush(max_heap, -n)
            elif -max_heap[0] > n:
                heapq.heappop(max_heap)
                heapq.heappush(max_heap, -n)
        
        return -max_heap[0]
                