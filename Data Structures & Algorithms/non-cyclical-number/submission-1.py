class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()
        while n not in visit:
            visit.add(n)
        # here notice that .add() is used insted of append(), because we are using set here not list or array
            n = self.sumofsquares(n) 
# n keeps getting updated, and we are checking everytime, have we reached 1?
            if n == 1:
                return True
        
        return False
#visit basically says:
#"Hey, I've seen this number before. We're going in circles."
# eg. n = 4. it goes 4 → 16 → 37 → 58 → 89 → 145 → 42 → 20 → 4 - see, we've reached 4 again and the cycle repeats,so we need to exit from the loop and tell the user that 4 is not a happy number, 4 is a cyclic number.
# visit = {4,16,37,58,89,145,42,20}
    def sumofsquares(self, n: int) -> int:

        sum = 0
        while n:
            a = n%10 # gives the last digit.
            sum += a**2
            n = n//10 # removes last digit, divide n by 10 twice in a row
        return sum
        
       
        