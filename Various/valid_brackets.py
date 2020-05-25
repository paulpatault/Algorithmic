"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid. 
An input string is valid if:
- Open brackets are closed by the same type of brackets.
- Open brackets are closed in the correct order.
- Note that an empty string is also considered valid.
"""


def peek(stack: list) -> int:
    return stack[len(stack) - 1]


class Solution:
    def isValid(self, s):
        arr = list(s)
        stack = []
        for ch in arr:
            if ch in ("{", "[", "("):
                stack.append(ch)
            elif ch == "]":
                if len(stack) == 0 or peek(stack) != "[":
                    return False
                stack.pop()
            elif ch == ")":
                if len(stack) == 0 or peek(stack) != "(":
                    return False
                stack.pop()
            elif ch == "}":
                if len(stack) == 0 or peek(stack) != "{":
                    return False
                stack.pop()
        return len(stack) == 0


# Test Program
s = "()(){(())"
# should return False
print(Solution().isValid(s))

s = ""
# should return True
print(Solution().isValid(s))

s = "([{}])()"
# should return True
print(Solution().isValid(s))
