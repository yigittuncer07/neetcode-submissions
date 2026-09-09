class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])

        queue = collections.deque()
        visited = set()

        directions = [(0,1),(1,0),(-1,0),(0,-1)]

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    queue.append((i,j))
                    visited.add((i,j))

        dist = 0
        while queue:
            for _ in range(len(queue)):
                ci, cj = queue.popleft()
                grid[ci][cj] = dist

                for di, dj in directions:
                    ni, nj = ci - di, cj - dj
                    if ni < 0 or nj < 0 or ni >= ROWS or nj >= COLS or (ni,nj) in visited or grid[ni][nj] == -1:
                        continue
                    queue.append((ni,nj))
                    visited.add((ni,nj))

            dist += 1
        