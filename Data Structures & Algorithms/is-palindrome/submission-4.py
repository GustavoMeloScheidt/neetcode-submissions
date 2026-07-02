class Solution:
    def isPalindrome(self, s: str) -> bool:
        # the logic for this solution is that we will go through the string
        # if it is an alphanumeric character, we will (after lowercasing it)
        # add it to the new string, and then it is the same as when reversed, it passes
        string = ''
        for c in s:
            if c.isalnum(): # if it constains alphanumeric characters 
                string += c.lower()
        return string == string[::-1]