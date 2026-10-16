class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        right = 1
        left = 0
        mxProf = 0

        while left < right and right <= len(prices)-1:
            if prices[right] < prices[left]:
                left = right;
                right+=1
            else: 
                profit = prices[right] - prices[left]
                right+=1
                mxProf = max(profit, mxProf)
        return mxProf
        