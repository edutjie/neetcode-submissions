class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        l_highest, r_highest = height[l], height[r]
        total_area = 0
        while l < r:
            if l_highest < r_highest:
                l += 1
                l_highest = max(l_highest, height[l])
                total_area += (l_highest - height[l])
            else:
                r -= 1
                r_highest = max(r_highest, height[r])
                total_area += (r_highest - height[r])

        return total_area

