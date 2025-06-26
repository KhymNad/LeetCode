from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Time: O(n) - we loop through the list once
        # Space: O(1) - we use a constant amount of extra space

        # Initialize min_price to a very large number so any price will be lower initially
        min_price = float('inf')

        # Initialize max_profit to 0, meaning no profit has been made yet
        max_profit = 0        

        # Loop through each price in the list
        for price in prices:

            # If the current price is less than the minimum we've seen,
            # update min_price to this new lower value
            if price < min_price:
                min_price = price

            # Calculate potential profit by selling at the current price
            profit = price - min_price

            # If this profit is greater than our previously recorded max profit,
            # update max_profit to this new higher value
            if profit > max_profit:
                max_profit = profit

        # After checking all prices, return the maximum profit found
        return max_profit
