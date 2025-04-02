class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        """The idea is to find min and sell on a day bigger than min next, then buy on the next min and sell on the next bigger day."""
        """Greedy Search"""
        total_profit = 0
        for i in range(len(prices) - 1):  
            if prices[i + 1] > prices[i]:
                total_profit += prices[i + 1] - prices[i]  
        return total_profit
