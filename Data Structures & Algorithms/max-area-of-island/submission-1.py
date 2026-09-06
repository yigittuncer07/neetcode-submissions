class Solution:

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        LEN_ROWS = len(grid)
        LEN_COLS = len(grid[0])
        
        visited = set()
        ans = 0
        
        for i in range(LEN_ROWS):
            for j in range(LEN_COLS):
                
                if grid[i][j] == 0 or (i,j) in visited:
                    continue
                
                current_area = 0
                stack = []
                stack.append((i,j))
                while stack:

                    curr = stack.pop()
                    
                    if curr in visited or curr[0] < 0 or curr[1] < 0 or curr[0] >= LEN_ROWS or curr[1] >= LEN_COLS or grid[curr[0]][curr[1]] == 0:
                        continue
                    visited.add((curr[0],curr[1]))
                    current_area += 1
                    
                    stack.append((curr[0], curr[1] + 1))         
                    stack.append((curr[0] + 1, curr[1]))
                    stack.append((curr[0], curr[1] - 1))
                    stack.append((curr[0] - 1, curr[1]))

                ans = max(ans, current_area)
        
        
        return ans
