class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        num_set = set(nums)

        sequence_starts = []

        for n in nums:
            if (n - 1) not in num_set:
                sequence_starts.append(n)
            
        max_seq = 1
        print(sequence_starts)
        for n in sequence_starts:
            seq = 1
            bflag = False
            nextn = n + 1
            while not bflag:
                if nextn in num_set:
                    seq += 1
                    max_seq = max(seq, max_seq)
                    nextn += 1
                else:
                    bflag = True

        return max_seq


        