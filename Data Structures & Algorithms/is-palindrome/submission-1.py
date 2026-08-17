class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        while l < r:
            sl = s[l]
            while not sl.isalnum() and l < r:
                l += 1
                sl = s[l]

            sr = s[r]
            while not sr.isalnum() and r > l:
                r -= 1
                sr = s[r]

            if sl.lower() != sr.lower():
                return False
            l += 1
            r -= 1
        return True
            

