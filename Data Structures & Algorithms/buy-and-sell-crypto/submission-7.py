'''
          b s
[10,2,6,3,1,5,6,7,1] 0
          b s 
[10,8,7,5,2] -3 < 0 return 0
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0

        buy = 0
        sell = 1

        profit = 0

        while sell < len(prices):
            if prices[sell] - prices[buy] < 0:
                buy = sell
            else:
                profit = max(profit,prices[sell]-prices[buy])
            
            sell+=1
        
        return profit
             
        