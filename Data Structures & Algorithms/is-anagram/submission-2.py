class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        stringS = []
        stringT = []

        for word in s:
            stringS.append(word)
        for word in t:
            stringT.append(word)
        stringS.sort()
        stringT.sort()
        if stringS == stringT:
            return True 
        return False
        