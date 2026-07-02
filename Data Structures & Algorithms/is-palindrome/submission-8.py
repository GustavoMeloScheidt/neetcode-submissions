class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Now, for this pointers solution, the idea is that we will have two pointers:
        # One at the beginning of the string and another at the end of the string
        # And for each step, we compare them to see if they are the same
        # Of course, we need to remove spaces and ponctuations, for that we have 
        # two ways to do it: either a .isalnum() function, or we build the alphaNumerical 
        # function, basing ourselves in the ASCII values
        l = 0 # Left Pointer
        r = len(s) - 1 # Right Pointer
        while l < r:
            while l < r and not self.AlphaNumerical(s[l]):
                l += 1
            while l < r and not self.AlphaNumerical(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l = l + 1
            r = r - 1
        return True

    # Creating our own AlphaNumerical function instead of using .isalnum():
    def AlphaNumerical(self, c):
        # In python we can get the ASCII value of a character by using the ord function
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or 
                ord('0') <= ord(c) <= ord('9'))
