"""
Implement a class for a stack that supports all the regular functions (push, pop) 
and an additional function of max() which returns the maximum element in the stack (return None if the stack is empty). 
Each method should run in constant time.
"""


class MaxStack:
    def __init__(self):
        self.stack = []
        self.maximum = None
        self.next = 0

    def push(self, val):
        self.stack.append(val)
        self.next += 1
        if self.maximum:
            self.maximum = max(self.maximum, val)
        else:
            self.maximum = val

    def pop(self):
        if self.next > 0:
            self.stack = self.stack[:-1]
            self.next -= 1
            if self.next == 0:
                self.maximum = None
            else:
                self.maximum = max(self.stack)

    def max(self):
        return self.maximum

    def empty(self):
        return self.next != 0


s = MaxStack()
s.push(1)
s.push(2)
s.push(3)
s.push(2)
print(s.max())
# 3
s.pop()
s.pop()
print(s.max())
# 2
