class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()
        answers = []        

        current = []
        def dfs(i, cur_target) -> None:
            if cur_target == 0:
                nonlocal answers
                answers.append(current.copy())
                return
            
            if i >= len(candidates):
                return 

            can = candidates[i]

            if cur_target - can < 0:
                while i + 1 < len(candidates) and candidates[i + 1] == candidates[i]:
                    i = i + 1
                
                dfs(i + 1, cur_target)
                return 
            
            current.append(can)
            dfs(i + 1, cur_target - can)

            current.pop()
            while i + 1 < len(candidates) and candidates[i + 1] == candidates[i]:
                i = i + 1
            dfs(i + 1, cur_target)

        dfs(0, target)

        return answers


