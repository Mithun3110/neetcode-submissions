class Solution:
    def isValid(self, s: str) -> bool:
        par = []
        close = {')': '(', '}': '{', ']': '['}

        for c in s:
            if c not in close:
                par.append(c)
                continue
            if par and par[-1] == close[c]:
                par.pop() 
            else :
                return False

        if not par:
            return True
        else:
            return False
            
