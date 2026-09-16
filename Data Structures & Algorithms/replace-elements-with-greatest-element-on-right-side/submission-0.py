class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        prev = -1
        temp = -1
        for i in range(len(arr) - 1, -1, -1):
            temp = arr[i]
            arr[i] = prev
            prev = max(temp, prev)

        return arr