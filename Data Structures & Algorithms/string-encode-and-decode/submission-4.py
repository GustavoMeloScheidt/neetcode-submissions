class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            stringW = str(len(word))
            res += stringW + "#" + word
        return res
        
    def decode(self, s: str) -> List[str]:            
        output = []
        i = 0

        while i < len(s):
            number = ""  
            
            while s[i] != "#":
                number += s[i]
                i += 1
            
            intNumber = int(number)
            i += 1  # skip the '#'
            
            output.append(s[i : i + intNumber])
            i = i + intNumber  # move past the word

        return output