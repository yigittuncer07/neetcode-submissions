class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        complimentLookupHashMap = {}
        for i in range(len(nums)):
            complement = target - nums[i]

            index = complimentLookupHashMap.get(complement)
            if index != None:
                return [index, i]
            else:
                complimentLookupHashMap[nums[i]] = i
        
        return []
