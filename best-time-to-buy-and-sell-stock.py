# Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = prices[0]
        profit = 0
        
        for price in prices:
            if price < low:
                low = price
            elif price > low and price - low > profit:
                profit = price -low
  
        return profit
