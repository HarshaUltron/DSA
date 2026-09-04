from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            # if we find smaller price, update min_price
            if price < min_price:
                min_price = price
            # calculate profit if we sell today
            elif price - min_price > max_profit:
                max_profit = price - min_price

        return max_profit

dt=Solution()
print(dt.maxProfit([7, 1, 5, 3, 6, 4]))