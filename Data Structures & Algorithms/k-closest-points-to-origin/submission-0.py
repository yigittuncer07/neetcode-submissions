class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []

        for point in points:
            distance = self._get_distance(point)

            if len(max_heap) < k:
                heapq.heappush(max_heap, (-distance, point))
            elif -max_heap[0][0] > distance:
                heapq.heappop(max_heap)
                heapq.heappush(max_heap, (-distance, point))

        return [element[1] for element in max_heap]

    def _get_distance(self, point: List[int]) -> int:
        x1, y1 = point[0], 0
        x2, y2 = 0, point[1]

        ans = (x1 - x2) ** 2
        ans += (y1 - y2) ** 2
        return ans ** 0.5