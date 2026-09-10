class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counterS, counterT = {}, {}
        if len(s) != len(t):
            return False 
        
        for i in range(len(s)): 
            # len(s) = 6  -> range(6) -> 0,1,2,3,4,5
            # counterS[s[0]] = counterS[s[0]].get(s[0], 0) + 1
            counterS[s[i]] = counterS.get(s[i], 0) + 1
            counterT[t[i]] = counterT.get(t[i], 0) + 1
        return counterS == counterT
