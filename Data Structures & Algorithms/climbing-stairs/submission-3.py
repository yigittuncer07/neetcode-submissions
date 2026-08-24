class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[-1] = 1
        dp[-2] = 1

        for i in range(len(dp) - 3, -1, -1):
            dp[i] = dp[i + 1] + dp[i + 2]

        return dp[0]


    # def climbStairs(self, n: int) -> int:

    #     hm = {}

    #     def dfs(steps):
    #         if steps == 0:
    #             return 1

    #         count = 0
            
    #         current = steps - 2
    #         if current >= 0:
    #             if current not in hm:
    #                 result = dfs(current)
    #                 hm[current] = result
                
    #             count += hm[current]
            
    #         current = steps - 1
    #         if current >= 0:
    #             if current not in hm:
    #                 result = dfs(current)
    #                 hm[current] = result
                
    #             count += hm[current]
    #         return count

    #     return dfs(n)