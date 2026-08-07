class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        buy, sell = 0, 1

        while sell < len(prices):
            profit = prices[sell] - prices[buy] 
            if profit < 0:
                buy = sell
                sell = buy + 1
            else:
                res = max(res, profit)
                sell += 1
        
        return res