class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        num_set = set(nums)

        max_seq = 1
        for n in nums:
            if (n - 1) not in num_set:
                seq = 1
                nextn = n + 1
                while nextn in num_set:
                    seq += 1
                    max_seq = max(seq, max_seq)
                    nextn += 1

        return max_seq


        