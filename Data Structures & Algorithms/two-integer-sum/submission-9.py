class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # here the idea is to use dictionaries to compare the sum
        # we use enumerate to get both the index and the value of each element
        # then we compare the complement (that we calculate) with the current number
        # if this complement is in the list, we return the pair, otherwise we continue
        # (and save the current number in seen)
        seen = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in seen:
                return [seen[complement],i]
                
            seen[num] = i