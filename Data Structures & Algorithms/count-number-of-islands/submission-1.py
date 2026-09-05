class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # dfs search, keep visited set, each DFS end is another island.

        ROWS_LEN = len(grid)
        COLUMNS_LEN = len(grid[0])
        visited = set()
        islands = 0 

        for i in range(ROWS_LEN):
            for j in range(COLUMNS_LEN):
                if grid[i][j] == '0' or (i,j) in visited:
                    continue
                
                islands += 1

                stack = []
                stack.append((i,j))

                while stack:
                    curr = stack.pop()
                    if curr[0] < 0 or curr[1] < 0 or curr[0] >= ROWS_LEN or curr[1] >= COLUMNS_LEN or grid[curr[0]][curr[1]] == '0' or (curr[0],curr[1]) in visited:
                        continue
                    visited.add((curr[0],curr[1]))
                    stack.append((curr[0] + 1,curr[1]))
                    stack.append((curr[0],curr[1] + 1))
                    stack.append((curr[0] - 1,curr[1]))
                    stack.append((curr[0],curr[1] -1))
        return islands

                
