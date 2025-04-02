class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # Track min price seen so far and max profit possible
        min_price, max_profit = prices[0], 0

        for price in prices:
            # Update min price (best time to buy)
            if price < min_price:
                min_price = price
            
            # Check if selling today gives better profit
            if price - min_price > max_profit:
                max_profit = price - min_price

        return max_profit
