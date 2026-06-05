class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0
        n=len(nums)
        for i in range(n):
            if farthest<i:
                return False
            farthest = max(farthest, i+nums[i])
        return farthest >= n-1
        