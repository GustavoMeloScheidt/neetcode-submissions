# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        current = head

        while current:
            if current in seen:
                return True
            # mesmo se tiverem valores repetidos na LL (head), ainda funciona
            # pois estamos guardando os objetos, nao os valores
            # ex: [1,2,1] -> como se fosse A(1), B(2), C(1),
            # aqui guardamos os objetos (endereço na memória) -> A, B, C
            seen.add(current)
            current = current.next

        return False
