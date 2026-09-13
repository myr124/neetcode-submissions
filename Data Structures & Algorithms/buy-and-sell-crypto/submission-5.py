class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L = 0
        R = L+1
        res = float("-inf")
        while R < len(prices):
            res = max(res, prices[R]-prices[L])
            if prices[L] > prices[R]:
                L=R
                R+=1
            else:
                R+=1

        return max(0,res)

        