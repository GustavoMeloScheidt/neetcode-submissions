class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums) # 3
        # n + 1 = 0, 1, 2, 3
        for i in range(n+1):
            if i not in nums:
                return i
