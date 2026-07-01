class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }

        for c in s:
            if c in closeToOpen:
                # matching the closed to the open
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            # if its just an opening parentheses, just keep going
            else:
                stack.append(c)
        #return true if its empty 
        return True if not stack else False