class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_height = 0
        for i, h in enumerate(heights):
            if not stack or stack[-1][1] <= h:
                stack.append([i,h])
            else:
                while stack and stack[-1][1] > h:
                    last = stack.pop()
                    max_height = max(last[1] * (i - last[0]), max_height)
                stack.append([last[0],h])
        while stack:
            last = stack.pop()
            max_height = max(last[1] * (len(heights) - last[0]), max_height)
        stack.append([last[0],h])
        return max_height
