class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        complimentLookupHashMap = {}
        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in complimentLookupHashMap:
                return [complimentLookupHashMap[complement], i]

            complimentLookupHashMap[nums[i]] = i
        
        return []
