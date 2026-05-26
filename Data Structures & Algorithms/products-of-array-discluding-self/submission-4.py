class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        current = 0

        while(current < len(nums)):
            b = 0
            product = 1
            while(b < len(nums)):
                if(b == current):
                    b+=1
                else:
                    product *= nums[b]
                    b+=1
            output[current] = product
            current+=1
        return output





        