class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dct = dict()
        for i, num in enumerate(sorted(nums)):
            dct[num] = dct.get(num-1, 0) + 1

        max_seq = 0
        for i in dct.values():
            max_seq = max(max_seq, i)

        return max_seq