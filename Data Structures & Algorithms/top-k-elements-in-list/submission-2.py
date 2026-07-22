class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}
        freq_arr = []
        for _ in range(len(nums) + 1):
            freq_arr.append([])

        for num in nums:
            freq_map[num] = freq_map.get(num,0) + 1
        
        for num, count in freq_map.items():
            freq_arr[count].append(num)

        result = []
        for i in range(len(freq_arr) - 1, 0, -1):
            for n in freq_arr[i]:
                result.append(n)
                if len(result) == k:
                    return result
                