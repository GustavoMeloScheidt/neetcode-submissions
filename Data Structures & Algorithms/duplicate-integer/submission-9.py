class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # so the logic is that
        # we will check every element for duplicates
        # and then we will use a data structure
        # that only holds only element (key)
        # if we check an element and it is already there
        # return True, otherwise return False

        seen = set()

        for i in nums:
            if i in seen:
                return True
            seen.add(i)
        return False
