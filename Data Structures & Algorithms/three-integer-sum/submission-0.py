class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        hm = {}
        for i,n in enumerate(nums):
            hm[n] = i

        found_triplets = set()

        ans = []
        for i, n in enumerate(nums):
            for j in range(i + 1, len(nums)):
                complement = -(nums[i] + nums[j])
                if complement in hm:
                    if hm[complement] != i and hm[complement] != j and tuple(sorted([nums[i], nums[j], complement])) not in found_triplets:
                        ans.append([nums[i],nums[j],complement])
                        found_triplets.add(tuple(sorted([nums[i], nums[j], complement])))
                        
            
        return ans



        