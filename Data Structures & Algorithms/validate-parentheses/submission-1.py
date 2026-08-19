class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_bracket_map = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        for c in s:
            if c in open_bracket_map:
                if len(stack) == 0 or stack[-1] != open_bracket_map[c]:
                    return False
                stack.pop()
            else:
                stack.append(c)

        return True if len(stack) == 0 else False
        