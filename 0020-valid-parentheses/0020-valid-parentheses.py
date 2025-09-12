class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        ref = {'}':'{', ']':'[', ')':'('}
        for i in s:
            if i in ref:
                if stack and stack[-1]==ref[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return not stack 
