class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictionaryS = {}
        dictionaryT = {}
        for i in s:
            # the logic is to add each string to the dictionary
            # and if we pass through them again, we increment the count
            dictionaryS[i] = dictionaryS.get(i,0) + 1

        for i in t:
            dictionaryT[i] = dictionaryT.get(i,0) + 1
        
        return dictionaryS == dictionaryT
