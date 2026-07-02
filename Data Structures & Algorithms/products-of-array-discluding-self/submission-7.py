class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1 
        finalOutput = []
        zero_count = 0 

        for i in nums:
            if i == 0:
                zero_count += 1
            else:
                prod = prod * i # 48
        if zero_count > 1:
            return [0] * len(nums)

        for i in nums:
            if zero_count == 1:
                if i == 0:
                    finalOutput.append(prod)
                else:
                    finalOutput.append(0)
            else:  
                finalOutput.append(prod // i)

        return finalOutput
            