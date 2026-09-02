class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # for every key created, an empty list is created
        for s in strs:
            count = [0]* 26
            for c in s:
                count[ord(c) - ord('a')] += 1 # a+=1 and a=+1 are not the same, former = [a =a+1] ; latter = [ a = 1]
            res[tuple(count)].append(s)
        return list(res.values())
        

        