class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i, j = 0, len(nums) - 1

        while i <= j:
            m = (i + j) // 2
            print(m)

            if nums[m] == target:
                return m

            # left is sorted
            if nums[i] <= nums[m]:
                if target < nums[m]:
                    if target < nums[i]:
                        i = m + 1
                    else:
                        j = m - 1
                else:
                    i = m + 1
            # right is sorted
            else:
                if target < nums[m]:
                    j = m - 1
                else:
                    if nums[j] < target:
                        j = m - 1
                    else:
                        i = m + 1
        return -1



        