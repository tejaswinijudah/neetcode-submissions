class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]# intial buying price
        maxprofit = 0 # profit shouldn't be -ve
        for sell in prices:
            if sell<buy:
                buy = sell #keeps buying price minimum
            maxprofit = max(maxprofit,sell-buy)# checks for the highest profit
        return maxprofit