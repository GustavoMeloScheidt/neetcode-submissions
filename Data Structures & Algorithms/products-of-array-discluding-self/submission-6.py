class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [0] * len(nums)
        suffix = [0] * len(nums)
        result = [0] * len(nums)

        prefix[0] = suffix[len(nums) - 1] = 1 # append 1 to the first and last element of prefix and suffix, respectively

        for i in range(1, len(nums)):
            prefix[i] = (nums[i - 1] * prefix[i - 1])

        for i in range(len(nums) - 2, -1, -1): 
            # the second parameter as "-1" is because we want to go all the way to the first element, but range is exclusive to the right element (for ex: range(5,8) is 5,6,7). So instead of putting "0", we put "-1"
            # the last "-1" is to indicate we're going from right to left
            suffix[i] = (nums[i + 1] * suffix[i + 1])
        
        for i in range(len(nums)):
            result[i] = prefix[i] * suffix [i]
        
        return result
        
