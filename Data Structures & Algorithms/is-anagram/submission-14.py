class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count_s, count_t = {}, {}

        # Usar o get é uma maneira mais facil de criar um dict 
        # (caso nao tenha) e incrementa-lo,pega um valor pela chave, igual:

    #    if char in count_s:
    #         count_s[char] = count_s[char] + 1
    #     else:
    #         count_s[char] = 1

        for i in s:
            count_s[i] = count_s.get(i, 0) + 1

        for i in t:
            count_t[i] = count_t.get(i, 0) + 1
        
        return count_s == count_t
            