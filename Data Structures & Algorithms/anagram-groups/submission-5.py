class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # defaultdict é uma forma de criar um dicionario, onde se a chave nao existir,
        # ele inicializa uma lista vazia (tipo o .get(i,0))
        anagrams = defaultdict(list)

        for s in strs:
            sortedS = ''.join(sorted(s))
            # a ideia é pegar um dicionario, fazer um sorted, e adicionar 
            # essas palavras ordenadas e adicionar elas à chave inicial
            # assim teremos uma chave (ordenada) com varios valores (iniciais da lista)
            anagrams[sortedS].append(s)
        return list(anagrams.values())
