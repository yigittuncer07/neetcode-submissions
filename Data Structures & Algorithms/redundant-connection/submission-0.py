class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        pars = [i for i in range(len(edges) + 1)]
        ranks = [1] * (len(edges) + 1)

        print(pars)
        
        def find(n):
            while n != pars[n]:
                n = pars[n]
                pars[n] = pars[pars[n]]
            return n

        def union(n1, n2):
            n1, n2 = find(n1), find(n2)

            if n1 == n2:
                return 0

            if ranks[n1] < ranks[n2]:
                pars[n1] = n2
                ranks[n2] += ranks[n1]
            else:
                pars[n2] = n1
                ranks[n1] += ranks[n2]    
            return 1
        
        for a, b in edges:
            if not union(a - 1,b - 1):
                return [a,b]