class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = prices[0]
        r = 1
        profit = 0
        while r < len(prices):
            current = prices[r]
            if current < low:
                low = current
            if current > low and current - low > profit:
                profit = current - low
            r += 1
        return profit