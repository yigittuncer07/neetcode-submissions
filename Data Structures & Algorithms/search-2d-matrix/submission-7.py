class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        i = 0
        j = len(matrix) - 1
        row = None

        while i <= j:
            m = (i + j) // 2

            if matrix[m][0] <= target and target <= matrix[m][-1]:
                j = -1
                row = matrix[m]
                continue
            
            if target < matrix[m][0]:
                j = m - 1
            else:
                i = m + 1

        if not row:
            return False
            
        i = 0
        j = len(row) - 1

        while i <= j:
            m = (i + j) // 2

            if row[m] == target:
                return True

            if target < row[m]:
                j = m - 1
            else:
                i = m + 1
        return False
        