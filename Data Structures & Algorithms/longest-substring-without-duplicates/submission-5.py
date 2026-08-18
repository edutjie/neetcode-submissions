class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique_char_map = dict()
        max_res = 0
        res = 0
        start_i = 0
        for i, c in enumerate(s):
            prev_i = unique_char_map.get(c, None)
            if prev_i is None or prev_i < start_i:
                res += 1
            else:
                max_res = max(max_res, res)
                res -= (prev_i - start_i)
                start_i = prev_i + 1
            unique_char_map[c] = i
        max_res = max(max_res, res)
        return max_res