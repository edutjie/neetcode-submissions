class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        outputs = set()
        for i in range(len(nums)):
            num_i = nums[i]
            l, r = i + 1, len(nums) - 1
            while l < r:
                num_l, num_r = nums[l], nums[r]
                sum_three = num_i + num_l + num_r
                if sum_three > 0:
                    r -= 1
                elif sum_three < 0:
                    l += 1
                else:
                    outputs.add((num_i, num_l, num_r))
                    r -= 1
                    l += 1
        return [list(o) for o in outputs]