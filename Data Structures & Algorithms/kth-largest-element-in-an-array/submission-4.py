class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # maxHeap = [-n for n in nums]

        # heapq.heapify(maxHeap)
        # cnt = 1
        # while cnt < k:
        #     heapq.heappop(maxHeap)
        #     cnt += 1
        
        # return -maxHeap[0]

        # QUICK SELECT ALGO 

        k = len(nums) - k

        def quickSelect(l,r):
            piv , p = nums[r], l
            for i in range(l,r):
                if nums[i] <= piv:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            
            nums[p],nums[r] = nums[r], nums[p]

            if p > k:
                return quickSelect(l,p-1)
            elif k > p:
                return quickSelect(p+1,r)
            else:
                return nums[p]
        
        return quickSelect(0,len(nums) - 1)