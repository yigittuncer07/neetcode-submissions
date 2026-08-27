class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        answers = []

        current = []
        def dfs(i, cur_tar):
            if cur_tar == 0:
                answers.append(current.copy())
                return
            
            if i >= len(nums):
                return

            if cur_tar - nums[i] < 0:
                dfs(i + 1, cur_tar)
                return

            current.append(nums[i])
            dfs(i, cur_tar - nums[i])

            current.pop()
            dfs(i + 1, cur_tar)

        dfs(0, target)
        return answers

            

            
        