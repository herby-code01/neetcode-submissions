class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0 
        r = len(heights) - 1
        mx = 0 

        while l < r:
            height = min(heights[l], heights[r])
            base = r - l
            area = base * height
            if heights[r] < heights[l]:
                r-=1
            else: 
                l+=1
            mx = max(area, mx)
        return mx