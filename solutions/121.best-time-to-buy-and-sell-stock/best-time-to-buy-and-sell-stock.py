class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        max_profit = 0
        
        days = len(prices)
        
        if days in [0,1]:
            return max_profit
        
        min_price = float("inf")
        
        for i in range(days):
            if prices[i] < min_price:
                min_price = prices[i]
            else:
                profit = prices[i] - min_price
                if profit > max_profit:
                    max_profit = profit
            
        return max_profit
    