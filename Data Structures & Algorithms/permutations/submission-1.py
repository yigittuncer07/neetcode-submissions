import random
import math


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = set()

        while len(ans) != math.factorial(len(nums)):
            random.shuffle(nums)

            if tuple(nums) not in ans:
                ans.add(tuple(nums))

        new_ans = []
        for item in ans:
            new_ans.append(list(item))
        return new_ans


        