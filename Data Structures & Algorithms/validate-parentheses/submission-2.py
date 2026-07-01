class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        
        openBrackets = set(['(','{','['])
        # Set only has keys, the {} has keys and value
        matchingParenthesis = {'(':')', '{':'}', '[':']'}

        stack = [] 

        for i in s:
            # count as many open as close 
            if i in openBrackets:
                stack.append(i)
            else:
                if stack and matchingParenthesis[stack[-1]]== i: # it means if stack is not empty (stack not none)                    
                    stack.pop()
                else: 
                    return False
        if stack:
            return False
        else: 
            return True

            


                