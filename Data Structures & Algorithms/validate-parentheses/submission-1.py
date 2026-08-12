class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False

        stack = []
        closeToOpen = {")": "(", "}": "{", "]": "["}

        for c in s:
            if c not in closeToOpen:
                stack.append(c)
            else:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
        
        return False if len(stack) else True
        