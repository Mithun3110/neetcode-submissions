class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = [-n for n in nums]

        heapq.heapify(maxHeap)
        cnt = 1
        while cnt < k:
            heapq.heappop(maxHeap)
            cnt += 1
        
        return -maxHeap[0]