class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-s for s in stones]

        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            x = -heapq.heappop(maxHeap)
            y = -heapq.heappop(maxHeap)

            if x != y:
                val = max(x,y) - min(x,y)
                heapq.heappush(maxHeap,-val)

        
        if maxHeap:
            return (-maxHeap[0])
        else:
            return 0