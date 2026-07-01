class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        
        #openBrackets = set(['(','{','['])
        # Set only has keys, the {} has keys and value
        matchingParenthesis = {'(':')', '{':'}', '[':']'}

        stack = [] 

        for i in s:
            # count as many open as close 
            if i in matchingParenthesis: #it will only look for the keys
                stack.append(i)
            else:
                if len(stack) > 0 and matchingParenthesis[stack[-1]]== i: # it means if stack is not empty (stack not none)                    
                    stack.pop()
                # another writing of if: if stack and matchingParenthesis....
                else: 
                    return False

        return len(stack) == 0
        
        #return not stack # if stack is empty: return True


            


                