class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            stringW = str(len(word))
            res += stringW + "#" + word
            print(res)
        return res
        
    def decode(self, s: str) -> List[str]:            
        output = []
        i = 0
        #len(s) = 14
        while i < len(s):
            number = ""
            while s[i] != "#":
                number += s[i]
                i += 1
            intNumber = int(number)

            output.append(s[i + 1: i + 1 + intNumber])
            i = i + 1 + intNumber 

        return output

        

