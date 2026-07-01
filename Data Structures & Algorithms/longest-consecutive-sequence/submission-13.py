class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        seen = set(nums)

        longest = 0

        if not nums: return 0
        
        for n in seen:
            if n - 1 not in seen:
                # n is the beginning of the sequence

                counter = 1
                while n + 1 in seen:
                    n+=1
                    counter +=1
                longest = max(counter,longest)

        return longest