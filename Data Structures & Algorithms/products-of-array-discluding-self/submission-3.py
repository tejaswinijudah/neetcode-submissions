class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod, zero_count = 1, 0
        for num in nums:
            if num!=0:
                prod *= num
            else:
                zero_count += 1
        if zero_count > 1:
            return [0]*len(nums)
        
        res = [0]*len(nums)
        for i,c in enumerate(nums):
            if zero_count!=0: # here zero_count = 1
                if c!=0:
                    res[i]= 0 
                else:
                    res[i] = prod
            else:
                res[i] = prod//c # integer division, gives result in integer, prod/c gives float. we need only integer.
        return res

# time complexity O(n)
# space complexity O(1) extra space, and O(n) for output array,
# // = floor division. 10//2 = 5. 10/2 = 5.0
#It removes the decimal part by taking the floor.
#But why not use // all the time?
#For positive numbers, it looks like truncating the decimal:

#7 // 2 = 3

#But with negative numbers:

# -7 // 2 = -4

# rather than -3, because Python floors toward negative infinity.

# For this particular problem, though, the important thing is that the numbers can be negative, so it's worth noting that prod // c still gives the exact integer quotient when c is a factor of prod—which it is in the no-zero case.

# For example:

# [-1, 2, 3]

# Total: prod = -6

# For c = 2:

#-6 // 2 = -3


# which is exactly what we want.

# So in this problem, prod // c is being used because the division is guaranteed to be exact and we want an integer result.   