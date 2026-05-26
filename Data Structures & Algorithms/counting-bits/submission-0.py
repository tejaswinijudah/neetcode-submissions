class Solution:
    def countBits(self, n: int) -> List[int]:
        res =[]
        for i in range(n+1):
            num = i
            count = 0
            while num:
                count+=1 # so number of iterations = number of set bits.
                num = num & (num-1) # right most 1 bit removed
            res.append(count)
        return res