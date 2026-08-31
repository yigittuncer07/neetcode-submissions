class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        pos_dia = set() # j - i
        neg_dia = set() # j + i
        columns = set()

        answer = []

        board = [["."] * n for _ in range(n)]

        def backtrack(i):
            if i == n:
                answer.append(["".join(row) for row in board].copy())
                return 
                
            for j in range(n):



                if j in columns or (j - i) in pos_dia or (j + i) in neg_dia:
                    continue


                board[i][j] = "Q"
                pos_dia.add(j - i)
                neg_dia.add(j + i)
                columns.add(j)

                backtrack(i + 1)

                board[i][j] = "."
                pos_dia.remove(j - i)
                neg_dia.remove(j + i)
                columns.remove(j)

        backtrack(0)
        return answer

                