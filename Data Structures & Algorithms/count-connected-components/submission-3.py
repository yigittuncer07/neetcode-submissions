class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        pars = [i for i in range(n)]
        ranks = [1] * n

        def find(num):
            while num != pars[num]:
                num = pars[num]
                num = pars[pars[num]]
            return num

        def union(n1, n2):
            n1, n2 = find(n1), find(n2)

            if n1 == n2:
                return 0
            
            if ranks[n1] > ranks[n2]:
                pars[n2] = pars[n1]
                ranks[n1] += ranks[n2]
            else:
                pars[n1] = pars[n2]
                ranks[n2] += ranks[n1]

            return 1
        
        ans = n
        for a,b in edges:
            if union(a,b):
                ans -= 1
        return ans
