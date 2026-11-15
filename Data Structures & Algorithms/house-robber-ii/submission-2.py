class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        

        def help(i, j):
            r1, r2 = 0, 0
            for n in range(i, j):
                r1, r2 = r2, max(r1+nums[n],r2)
            return r2
        
        
        return max(nums[0],help(0, n-1),help(1, n))