class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        adj_list = {i:[] for i in range(n)}

        for a, b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)

        visited, cycle = set(), set()

        def dfs(node, prev):

            if node in cycle:
                return False
            if node in visited:
                return True

            cycle.add(node)

            for nei in adj_list[node]:
                if nei == prev:
                    continue
                if not dfs(nei, node):
                    return False
            
            cycle.remove(node)
            visited.add(node)

            return True
            
        return dfs(0, -1) and n == len(visited)