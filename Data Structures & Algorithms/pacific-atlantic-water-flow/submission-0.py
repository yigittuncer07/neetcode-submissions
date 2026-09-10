class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])

        deq = collections.deque()
        visited = set()

        # start with pacific nodes
        pacific_nodes = [(0, j) for j in range(COLS)] + [(i,0) for i in range(ROWS)]
        deq.extend(pacific_nodes)
        for n in pacific_nodes:
            visited.add(n) 
        pacific_reachable = set()

        while deq:
            ci, cj = deq.popleft()
            pacific_reachable.add((ci,cj))

            directions = [(0,1), (0,-1), (1,0), (-1,0)]
            for di, dj in directions:
                ni, nj = ci + di, cj + dj
                if nj < 0 or ni < 0 or nj >= COLS or ni >= ROWS or (ni,nj) in visited or heights[ni][nj] < heights[ci][cj]:
                    continue
                deq.append((ni,nj))
                visited.add((ni,nj))

        # start with pacific nodes
        atlantic_nodes = [(ROWS - 1, j) for j in range(COLS)] + [(i,COLS - 1) for i in range(ROWS)]
        deq.extend(atlantic_nodes)
        visited.clear()
        for n in atlantic_nodes:
            visited.add(n)

        atlantic_reachable = set()

        while deq:
            ci, cj = deq.popleft()
            atlantic_reachable.add((ci,cj))

            directions = [(0,1), (0,-1), (1,0), (-1,0)]
            for di, dj in directions:
                ni, nj = ci + di, cj + dj
                if nj < 0 or ni < 0 or nj >= COLS or ni >= ROWS or (ni,nj) in visited or heights[ni][nj] < heights[ci][cj]:
                    continue
                deq.append((ni,nj))
                visited.add((ni,nj))

        ans = []
        for val in atlantic_reachable:
            if not pacific_reachable:
                break
            if val in pacific_reachable:
                ans.append(list(val))
        return ans
            
 