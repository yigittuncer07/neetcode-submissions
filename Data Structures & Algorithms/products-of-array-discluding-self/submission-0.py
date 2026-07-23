class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        full_product = 1

        zero_flag = False
        for n in nums:
            if zero_flag and not n:
                return [0] * len(nums)
            if not n:
                zero_flag = True
                continue
            full_product *= n

        answer = []
        
        for n in nums:

            if zero_flag and not n:
                answer.append(full_product)
            elif zero_flag:
                answer.append(0)
            else:
                answer.append(int(full_product / n))
        return answer


        