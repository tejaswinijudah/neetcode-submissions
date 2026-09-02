class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # for every key created, an empty list is created
        for s in strs:
            sortedS = ''.join(sorted(s)) # ''.join() - basically joins shit with whatever is inside the quote, here, ntg is there. 
            # sorted(s) = ['a','e','t'] - gives characters in list. that list is joined as a string using ''.join()
            res[sortedS].append(s)
        return list(res.values())
        

        