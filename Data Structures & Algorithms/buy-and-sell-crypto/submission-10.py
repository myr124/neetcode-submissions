'''
you are given an integer array prices where prices[i] is the price of neetcoin on the ith day

You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.

Return the maximum profit you can achieve. You may choose to not make any 
transactions, in which case the profit would be 0.

brute force:
go through every number and calculate profit or loss at every other day return max 
value we get from that

downsides:
o(n^2) solution
tons of repeated work

optimized


 l  r           
[10,1,5,0,7,0,1]

profit = 4
profit = 5
profit = 6
profit = 0


- if value in right is lesser we move left to right and then right = right + 1

'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0, 1
        res = 0

        while r < len(prices):
            
            res = max(prices[r] - prices[l], res)

            if prices[r] < prices[l]:
                l = r
        
            r = r + 1

        return res

        





             
        