class Solution:
    def trap(self, height: List[int]) -> int:
        biggest_left = []
        biggest = 0
        for n in height:
            biggest_left.append(biggest)
            biggest = max(n,biggest)

        biggest_right = []
        biggest = 0
        for n in height[::-1]:
            biggest_right.append(biggest)
            biggest = max(n,biggest)
        biggest_right.reverse()

        ans = 0
        for i,n in enumerate(height):
            smallest_boundry = min(biggest_left[i],biggest_right[i])
            if n < smallest_boundry:
                ans += smallest_boundry - n

        return ans