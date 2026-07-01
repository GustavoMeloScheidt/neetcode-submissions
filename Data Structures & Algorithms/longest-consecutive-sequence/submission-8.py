class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        seen = set(nums)
        seen = sorted(seen)

        longest = 1
        counter = 1

        if not nums: return 0

        for n in seen: #for i in range(6)
            if n + 1 in seen: #if nums[1] (2)  + 1 == nums[2] (3)
                counter +=1
                longest = max(counter,longest)
            else:
                counter = 1
        return longest
