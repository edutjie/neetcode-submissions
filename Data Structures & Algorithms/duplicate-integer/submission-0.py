class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map_dct = dict()
        for num in nums:
            map_dct[num] = map_dct.get(num, 0) + 1
            if map_dct[num] > 1:
                return True
        return False