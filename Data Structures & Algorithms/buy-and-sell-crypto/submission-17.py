class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0 
        right = 1
        mxProfit = 0

        while right < len(prices):
            if prices[left] > prices[right]:
                left = right
                right +=1
            elif prices[right] >= prices[left]:
                profit = prices[right]- prices[left]
                mxProfit = max(profit, mxProfit)
                right +=1
                
                
        return mxProfit
                
            