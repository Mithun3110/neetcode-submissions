class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        res=""
        reslen = 0
        def help(l, r):
            nonlocal res, reslen
            while(l >=0) and (r< n) and s[l] == s[r]:
                if (r -l + 1) > reslen:
                    res = s[l:r+1]
                    reslen = r -l + 1
                l -= 1
                r += 1 
        for i in range(n):
            help(i, i)
            help(i, i +1)
        
        return res
            