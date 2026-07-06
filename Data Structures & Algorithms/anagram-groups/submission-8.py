class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Using the logic that we can count how many characters are in 
        # each string and then we can combine the characters with the 
        # same amount together (by adding them into a dictionary)
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26 
            for c in s:
                count[ord(c) - ord("a")] += 1 # here we did the substraction to go from values 0(a) to 25(z)
            # since our count is a lit, but lists cannot be keys, we change it to a tuple
            # res[count].append(s)
            res[tuple(count)].append(s)

        return list(res.values())
