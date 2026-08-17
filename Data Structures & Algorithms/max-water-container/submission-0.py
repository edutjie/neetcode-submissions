class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_area = 0
        while l < r:
            h_l, h_r = heights[l], heights[r]
            area = (r-l) * min(h_l, h_r)
            max_area = max(max_area, area)
            if h_l < h_r:
                l += 1
            else:
                r -= 1
        
        return max_area