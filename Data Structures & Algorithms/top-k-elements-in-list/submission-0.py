class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for i in nums:
            count[i] = count.get(i, 0) + 1

        sortedDict = dict(sorted(count.items(), key = lambda item: item [1], reverse = True)) #sort by value 

        sortedList = list(sortedDict.keys())
        
        result = []

        for i in range(k):
            result.append(sortedList[i])
        return result 



