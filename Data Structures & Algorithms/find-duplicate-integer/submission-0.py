class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums_map = defaultdict(bool)
        for num in nums:
            if nums_map[num]:
                return num
            nums_map[num] = True

        return nums[0]

            