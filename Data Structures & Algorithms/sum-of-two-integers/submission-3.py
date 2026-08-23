class Solution:
    def getSum(self, a: int, b: int) -> int:
        max_int = 0x7FFFFFFF
        mask = 0xFFFFFFFF
        while b != 0:
            carry = (a&b) << 1
            a = (a^b) & mask
            b = carry & mask
        return a if a <= max_int else ~(a^mask) 
        