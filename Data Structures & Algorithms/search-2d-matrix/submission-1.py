class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        mega_list = []

        for l in matrix:
            mega_list.extend(l)

        i = 0
        j = len(mega_list) - 1

        while i <= j:
            m = (i + j) // 2

            if mega_list[m] == target:
                return True

            if target < mega_list[m]:
                j = m - 1
            else:
                i = m + 1
        return False
        