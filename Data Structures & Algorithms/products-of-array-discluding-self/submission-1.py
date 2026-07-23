class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_product = []
        product = 1
        for n in nums:
            product *= n
            prefix_product.append(product)
        
        print(prefix_product)
        
        product = 1
        suffix_product = [0] * len(nums)
        for i in range(len(nums) - 1, -1 , -1):
            product *= nums[i]
            suffix_product[i] = product

        print(suffix_product)
        answer = []
        for i, n in enumerate(nums):
            product = 1
            if i > 0:
                product *= prefix_product[i - 1]
            if i + 1 < len(nums):
                product *= suffix_product[i + 1]
            answer.append(product)
        return answer







    def easyProductExceptSelf(self, nums: List[int]) -> List[int]:

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
