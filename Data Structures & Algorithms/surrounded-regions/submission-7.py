class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])

        def dfs(i, j, visited):
            stack = []

            stack.append((i,j))
            visited.add((i,j))

            mark = True

            while stack:
                ci, cj = stack.pop()
                on_border = (ci == 0 or ci == ROWS - 1 or cj == 0 or cj == COLS - 1)
                mark = not on_border and mark

                directions = [(0,1),(1,0),(-1,0),(0,-1)]
                for di, dj in directions:
                    ni, nj = ci + di, cj + dj
                    if ni < 0 or nj < 0 or ni >= ROWS or nj >= COLS or board[ni][nj] == "X" or (ni,nj) in visited:
                        continue
                    stack.append((ni,nj))
                    visited.add((ni,nj))
            return mark


        processed = set()

        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == "X" or (i,j) in processed:
                    continue
                visited = set()
                mark = dfs(i,j, visited)
                if mark:
                    for vi, vj in visited:
                        board[vi][vj] = "X"
                else:                        
                    for v in visited:
                        processed.add(v)