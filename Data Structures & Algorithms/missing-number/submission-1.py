class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        hash_set = set(nums)
        for i in range(n):
            if i not in hash_set:
                return i
        return n