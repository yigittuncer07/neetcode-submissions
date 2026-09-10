class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        stack = []
        stack.extend((0,j) for j in range(COLS) if board[0][j] == "O")
        stack.extend((ROWS - 1,j) for j in range(COLS) if board[ROWS - 1][j] == "O")
        stack.extend((i,0) for i in range(ROWS) if board[i][0] == "O")
        stack.extend((i,COLS - 1) for i in range(ROWS) if board[i][COLS - 1] == "O")

        
        visited = set()
        visited.update(stack)

        while stack:

            ci, cj = stack.pop()

            directions = [(0,1),(1,0),(-1,0),(0,-1)]
            for di, dj in directions:
                ni, nj = ci + di, cj + dj
                if ni < 0 or nj < 0 or ni >= ROWS or nj >= COLS or board[ni][nj] == "X" or (ni,nj) in visited:
                    continue
                stack.append((ni,nj))
                visited.add((ni,nj))

        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == "X" or (i,j) in visited:
                    continue
                board[i][j] = "X"            


