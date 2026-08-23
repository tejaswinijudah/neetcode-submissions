class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            binary = (n >> i) & 1
            res = res | (binary << (31-i))
        return res
        