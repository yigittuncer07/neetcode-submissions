

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums) - 1

        while i <= j:
            middle_index = ((j - i) // 2) + i
            if target == nums[middle_index]:
                return middle_index
            
            if target < nums[middle_index]:
                j = middle_index - 1
            else:
                i = middle_index + 1
        return -1


            