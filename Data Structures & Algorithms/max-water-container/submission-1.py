class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        mx = 0
        
        while left < right:
            h = min(heights[left], heights[right])
            b = right - left
            area = h * b
            
            mx = max(mx, area)
            if heights[left] < heights[right]:
                left+=1
            else:
                right-=1
        return mx
        
