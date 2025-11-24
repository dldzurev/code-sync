class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_buy = 99999
        for p in prices:
            if max_profit < (p - min_buy): max_profit = p - min_buy
            if min_buy > p: min_buy = p
        return max_profit