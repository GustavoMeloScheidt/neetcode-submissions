class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counterS = {}
        counterT = {}
        for i in s:
            counterS[i] = counterS.get(i, 0) + 1
            if i in counterS:
                counterS[i] +=1
            else:
                counterS[i] = 0
        for i in t:
            counterT[i] = counterT.get(i, 0) + 1
            if i in counterS:
                counterT[i] +=1
            else:
                counterT[i] = 0
        
        return counterS == counterT
        
            
            