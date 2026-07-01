class Solution:
    def isValid(self, s: str) -> bool:
    # the ideia is:
    # create a match for the parenthesis and then an empty stack, 
    # go through the match 1 by 1
    # if it is an open bracket, add it to the stack
    # it it is closed bracket, we compare it to the last element on the stack, 
    # if they match, pop them, otherwise return false 
        brackets = {'(':')', '{':'}', '[':']'}
        stack = []
        for i in s:
            if i in brackets:
                stack.append(i)
            else:
                if len(stack) > 0 and brackets[stack[-1]] == i:
                    stack.pop()
                else:
                    return False
                
        
        return len(stack) == 0