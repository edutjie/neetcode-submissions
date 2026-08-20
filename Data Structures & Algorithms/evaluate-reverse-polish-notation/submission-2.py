import operator

# Define a mapping of string operators to their corresponding functions
OPERATORS = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": lambda a, b: int(a / b),
    "//": operator.floordiv,
    "**": operator.pow,
}

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # operators = "+ - * /".split()
        stack = []
        for t in tokens:

            if t in OPERATORS:
                b = stack.pop()
                a = stack.pop()
                res = OPERATORS[t](a, b)
                stack.append(res)
            else:
                stack.append(int(t))
            
        if stack:
            return stack[-1]
        else:
            return 0