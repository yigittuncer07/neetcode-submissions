class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adj_list = {i:[] for i in range(n)}

        for a,b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)


        visited = set()
        ans = 0

        for i in range(n):
            if i in visited:
                continue
            deq = collections.deque()
            deq.append(i)
            visited.add(i)

            while deq:

                curr = deq.popleft()
                visited.add(curr)
                for nei in adj_list[curr]:
                    if nei not in visited:
                        deq.append(nei)
                    
            ans += 1
        return ans