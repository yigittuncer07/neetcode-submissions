class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1

        while True:
            if numbers[i] + numbers[j] > target:
                j -= 1
                continue
            elif numbers[i] + numbers[j] < target:
                i += 1
                continue
            
            return [i+1,j+1]
        