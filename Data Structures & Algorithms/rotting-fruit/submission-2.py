class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        queue = collections.deque()
        seen = set()
        total_fresh = 0

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    queue.append((i,j))
                    seen.add((i,j))
                elif grid[i][j] == 1:
                    total_fresh += 1

        steps = 0
        while queue:
            step_taken = False
            for _ in range(len(queue)):
                ci, cj = queue.popleft()
                if grid[ci][cj] == 1:
                    total_fresh -= 1
                    step_taken = True

                directions = [(0,1),(0,-1),(1,0),(-1,0)]
                for di, dj in directions:
                    ni, nj = ci + di, cj + dj
                    if ni < 0 or nj < 0 or ni >= ROWS or nj >= COLS or (ni,nj) in seen or grid[ni][nj] == 0:
                        continue
                    queue.append((ni,nj))
                    seen.add((ni,nj))
            if step_taken:
                steps += 1
        
        if total_fresh:
            return -1
        return steps