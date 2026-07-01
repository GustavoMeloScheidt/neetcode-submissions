class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # primeiro o set é criado, como não tem valores duplicados, o set ([1, 2, 3, 3]) vira ([1, 2, 3])
        # len(nums) so conta o numero, então é 4
        return len(set(nums)) != len(nums)