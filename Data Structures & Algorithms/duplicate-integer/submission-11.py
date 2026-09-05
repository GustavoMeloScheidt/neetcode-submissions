class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        lista = set(nums)

        return not len(lista) == len(nums)