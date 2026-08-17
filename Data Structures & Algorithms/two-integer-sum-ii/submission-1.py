class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1
        while l < r:
            nl, nr = numbers[l], numbers[r]
            sum_lr = nl + nr
            if sum_lr > target:
                r -= 1
            elif sum_lr < target:
                l += 1
            else:
                return [l+1, r+1]