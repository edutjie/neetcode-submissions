class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_buy, max_sell = prices[0], prices[0]
        max_profit = 0
        for p in prices:
            if p < min_buy:
                max_profit = max(max_profit, max_sell - min_buy)
                min_buy = max_sell = p
            if p > max_sell:
                max_sell = p

        return max(max_profit, max_sell - min_buy)

            