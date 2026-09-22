class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        pre = 1

        for n in range(len(nums)):
            output[n] =  pre
            pre *= nums[n]
        post = 1
        for n in range(len(nums)-1, -1, -1):
            output[n] *= post 
            post *= nums[n]

        return output