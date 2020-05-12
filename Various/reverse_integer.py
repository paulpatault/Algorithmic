"""
Given a 32-bit signed integer, reverse digits of an integer.
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            s = str(x)
            s = s[1:]
            a = int(s[::-1])
            return -a
        else:
            s = str(x)
            return int(s[::-1])


print(Solution().isPalindrome(123))
print(Solution().isPalindrome(-321))
