class Solution:
    def climbStairs(self, n: int) -> int:

        hm = {}

        def dfs(steps):
            if steps == 0:
                return 1

            count = 0
            
            current = steps - 2
            if current >= 0:
                if current not in hm:
                    result = dfs(current)
                    hm[current] = result
                
                count += hm[current]
            
            current = steps - 1
            if current >= 0:
                if current not in hm:
                    result = dfs(current)
                    hm[current] = result
                
                count += hm[current]
            return count

        return dfs(n)