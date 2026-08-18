class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = dict()
        l = 0
        max_freq = 0
        res = 0
        for r, c in enumerate(s):
            counter[c] = counter.get(c, 0) + 1
            max_freq = max(max_freq, counter[c])

            while ((r-l+1)-max_freq) > k:
                counter[s[l]] -= 1
                l += 1

            res = max(r-l+1, res)
        return res