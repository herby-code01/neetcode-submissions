class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        mxProf = 0

        while right < len(prices):
            if prices[right] < prices[left]:
                left = right
                right+=1
            else: 
                profit = prices[right] - prices[left]
                mxProf = max(mxProf, profit)
                right+=1
        return mxProf 

