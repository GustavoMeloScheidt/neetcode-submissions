class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        stringS, stringT= [], []

        for word in s:
            stringS.append(word)
        for word in t:
            stringT.append(word)
        stringS.sort()
        stringT.sort()

        return stringS == stringT
        