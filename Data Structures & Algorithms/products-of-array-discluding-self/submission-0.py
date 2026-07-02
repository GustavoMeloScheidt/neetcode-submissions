class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = 1
        zero_count = 0
        finalOutput = []

        for i in nums:
            if i == 0:
                zero_count += 1              
            else:
                res = res * i
        
        if zero_count > 1:
            return [0] * len(nums)
        
        #oneZero = [0] * len(nums)
        for j in nums:
            if zero_count == 1:
                if j == 0:
                    finalOutput.append(res)
                else:
                    finalOutput.append(0)
            else:
                finalOutput.append(res // j)
        return finalOutput
            