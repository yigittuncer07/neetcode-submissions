class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if not len(nums):
            return []

        nums.sort()
        
        current = []
        subsets = []
        
        def dfs(i):
            if i >= len(nums):
                return  
            
            current.append(nums[i])
            subsets.append(current.copy())

            dfs(i + 1)

            skip = current.pop()
            while i + 1 < len(nums) and nums[i + 1] == skip:
                i += 1

            dfs(i + 1)

        dfs(0)
        subsets.append([])
        return subsets