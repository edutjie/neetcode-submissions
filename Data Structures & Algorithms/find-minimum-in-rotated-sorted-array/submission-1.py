class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1

        while l < r:
            # mid = (l + r) // 2
            if nums[l] <= nums[r]:
                return nums[l]
            else:
                l += 1
                if nums[r-1] < nums[r]:
                    r -= 1
                else:
                    return nums[r]
        
        return nums[l]
