class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # l, r =  0,1
        # maxP  = 0
        # while r < len (prices):
        #     if prices[l] < prices[r]:
        #         profit = prices[r] - prices[l]
        #         maxP = max (maxP, profit)
        #     else:
        #         l= r
        #     r += 1
        # return maxP
     
        maxPro = 0
        minPrice = float('inf')
        for i in range(len(prices)):
            minPrice = min(minPrice, prices[i])
            maxPro = max(maxPro, prices[i] - minPrice)
        return maxPro