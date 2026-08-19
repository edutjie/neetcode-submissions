class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        s1_counter = dict()
        for c1 in s1:
            s1_counter[c1] = s1_counter.get(c1, 0) + 1

        s2_counter = dict()
        for i in range(len(s2) - len(s1) + 1):
            if len(s2_counter) == 0:
                for j in range(i, i + len(s1) - 1):
                    s2_counter[s2[j]] = s2_counter.get(s2[j], 0) + 1
            s2_counter[s2[i + len(s1) - 1]] = s2_counter.get(s2[i + len(s1) - 1], 0) + 1
            if s1_counter == s2_counter:
                return True
            s2_counter[s2[i]] -= 1
            if s2_counter[s2[i]] == 0:
                del s2_counter[s2[i]]
        return False