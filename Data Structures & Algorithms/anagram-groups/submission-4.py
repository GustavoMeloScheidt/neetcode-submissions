class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # the idea here is that we will sort the strings
        anagrams = defaultdict(list)
        
        for s in strs:
            # quando usamos sorted em uma string, para "eat"
            # ele devolve ['a', 'e', 't'], porque sorted() devolve uma lista

            # ''.join(['a','e','t']) vira "aet"
            # "separador".join(lista): o texto antes do .join() é o separador que será colocado entre os elementos.
            # ex: 
            # ','.join(['a', 'e', 't']) retorna 'a,e,t'
            sortedS = ''.join(sorted(s))

            # now, here we will use the sorted word as a key, and then we will append all the 
            # original words as values, because at the end we will return only the values (original words)
            # grouped by the keys
            # example, if we do anagrams["aet"].append("eat"), and then anagrams["aet"].append("eat")...
            # { "aet": ["eat", "tea", "ate"] }
            anagrams[sortedS].append(s)
        return list(anagrams.values())

        # a final organization of a dictionary would be:
        # {"aet": ["eat", "tea", "ate"],
          #"ant": ["tan", "nat"],
          #"abt": ["bat"]}

            