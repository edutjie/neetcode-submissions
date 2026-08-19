class MinStack:

    def __init__(self):
        self.stack = []
        self.min_element_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.min_element_stack) == 0 or val < self.stack[self.min_element_stack[-1]]:
            self.min_element_stack.append(len(self.stack)-1)

    def pop(self) -> None:
        if self.min_element_stack[-1] == len(self.stack)-1:
            self.min_element_stack.pop()
        removed_el = self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stack[self.min_element_stack[-1]]
        
