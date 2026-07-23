class MinStack:

    def __init__(self):
        self.stack = []
        self.extraStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        extraAppend = val
        if self.extraStack:
            extraAppend = min(val, self.extraStack[-1])
        self.extraStack.append(extraAppend)


    def pop(self) -> None:
        self.stack.pop(-1)
        self.extraStack.pop(-1)
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.extraStack[-1]
