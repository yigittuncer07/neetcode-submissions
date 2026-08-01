class Solution:
    def findMin(self, nums: List[int]) -> int:
        i = 0
        j = len(nums) - 1

        while i <= j:
            m = (i + j) // 2

            if nums[0] < nums[m] and nums[m] < nums[-1]:
                return nums[0]

            if (nums[m] < nums[m - 1] if (m - 1) >= 0 else True) and (nums[m] < nums[m + 1] if m + 1 < len(nums) else True):
                return nums[m]
            elif nums[0] <= nums[m]:
                i = m + 1
            elif nums[m] <= nums[-1]:
                j = m - 1
