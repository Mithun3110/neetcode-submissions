class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dupe = {}

        for n in nums:
            dupe[n] = dupe.get(n, 0 ) + 1

            if dupe[n] > 1:
                return n
        