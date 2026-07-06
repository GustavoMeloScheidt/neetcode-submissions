class Solution:
    def isPalindrome(self, s: str) -> bool:
        leftPointer = 0
        rightPointer = len(s) - 1

        while leftPointer < rightPointer:
        
            while leftPointer < rightPointer and not self.AlphaNumerical(s[leftPointer]):
                leftPointer +=1
            while rightPointer > leftPointer and not self.AlphaNumerical(s[rightPointer]):
                rightPointer -= 1
            
            if s[leftPointer].lower() != s[rightPointer].lower():
                return False
                
            leftPointer += 1
            rightPointer -= 1

        return True
    
    def AlphaNumerical(self, c):
            return (ord('A') <= ord(c) <= ord('Z') or
                    ord('a') <= ord(c) <= ord('z') or 
                    ord('0') <= ord(c) <= ord('9'))
