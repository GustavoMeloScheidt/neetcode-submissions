class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1 
        res = []
        zero_count = 0 
        for i in nums:
            if i == 0:
                zero_count +=1
            else:
                prod *= i # this means prod = prod * i
        if zero_count > 1:
            return [0] * len(nums)
        for j in nums:
            if zero_count == 1:
                if j == 0:
                    res.append(prod)
                else:
                    res.append(0)
            else:
                res.append(prod // j)
        return res

