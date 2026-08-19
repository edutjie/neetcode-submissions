class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        t_counter = dict()
        for i, c in enumerate(t):
            t_counter[c] = t_counter.get(c, 0) + 1
            # t_counter[c] = max(t_counter.get(c, 0), i)

        char_counter = dict()
        idx_stack = []
        l = 0
        res_idx = (-1, -1)
        res_len = float('inf')
        have = 0
        need = len(t_counter)
        for r, c in enumerate(s):
            if t_counter.get(c, None):
                char_counter[c] = char_counter.get(c, 0) + 1
                if char_counter[c] == t_counter[c]:
                    have += 1

            while have == need:
                if (r-l+1) < res_len:
                    res_idx = (l, r)
                    res_len = r-l+1

                
                if s[l] in char_counter:
                    char_counter[s[l]] -= 1
                    if char_counter[s[l]] < t_counter[s[l]]:
                        have -= 1

                l += 1
                
        if res_len == float('inf'):
            return ""
        return s[res_idx[0]:res_idx[1]+1]