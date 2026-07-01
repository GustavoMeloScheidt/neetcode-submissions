class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        stringS, stringT= [], []

        for i in range(len(s)):
            stringS.append(s[i])
            stringT.append(t[i])
        stringS.sort()
        stringT.sort()

        return stringS == stringT
        