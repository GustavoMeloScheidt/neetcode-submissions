class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(nums)):
            seen[nums[i]] = i


        for i, num in enumerate(nums):
            complement = target - num # 4

            if complement in seen and seen[complement] != i:
                return [i, seen[complement]]

            #seen[num] = i

            