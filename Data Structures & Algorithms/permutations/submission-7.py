import random
import math


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        ans = []
        current_set = set(nums)
        current_permutation = []
        def dfs():

            if not current_set:
                ans.append(current_permutation.copy())
                return 

            
            for num in list(current_set): 
                current_set.remove(num)
                current_permutation.append(num)
                dfs()
                current_set.add(num)
                current_permutation.pop()

        dfs()
        return ans

            






    # JOKE SOLUTION, obviously not optimal
    # def permute(self, nums: List[int]) -> List[List[int]]:
    #     ans = set()

    #     while len(ans) != math.factorial(len(nums)):
    #         random.shuffle(nums)

    #         if tuple(nums) not in ans:
    #             ans.add(tuple(nums))

    #     new_ans = []
    #     for item in ans:
    #         new_ans.append(list(item))
    #     return new_ans


        