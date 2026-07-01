# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            #abrir esquerda
            #abrir direita
            #retornar tamanho (return maior_anterior + 1 )
            if root is None:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)
            return max(left, right) + 1
            # se tirarmos o return max e deixar so os dois dfs, 
            # vemos que ele retorna em profudidade a arvore
            print (root.val)         
        return dfs(root)