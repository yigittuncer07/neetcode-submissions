class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []

        current = []
        def dfs(i):
            if i >= len(nums):
                subsets.append(current.copy())
                return
            
            # with i
            current.append(nums[i])
            dfs(i + 1)

            current.pop()
            dfs(i + 1)
        
        dfs(0)
        return subsets 



        