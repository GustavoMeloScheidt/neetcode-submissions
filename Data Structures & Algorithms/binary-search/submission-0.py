class Solution:
    def search(self, nums: List[int], target: int) -> int:
        x = len(nums) // 2 # if nums is 6 elements, x is 3 
        # go to i[x] 
        #     compare i[x] with the target 
        #         if its lower than target   
        #             forget about the content of the left
        #                 go to the middle of the remaining "right " side 
        # I need to have 2 pointers: 1 left and 1 right 
        lPointer = 0
        rPointer = len(nums) - 1
        while lPointer <= rPointer: 
            mPointer = (lPointer + rPointer) // 2 
            if nums[mPointer] == target:
                return mPointer
            elif nums[mPointer] < target:
                lPointer = mPointer + 1
            else:
                rPointer = mPointer - 1

        return -1 


