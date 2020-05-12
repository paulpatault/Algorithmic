"""
Determine whether an integer is a palindrome. 
An integer is a palindrome when it reads the same backward as forward.
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        return s == s[::-1]


print(Solution().isPalindrome(121))
print(Solution().isPalindrome(-121))
