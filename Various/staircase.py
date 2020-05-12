"""
You are given a positive integer N which represents the number of steps in a staircase. 
You can either climb 1 or 2 steps at a time. 
Write a function that returns the number of unique ways to climb the stairs.

"""


class Solution:
    def staircase(self, n):
        def rec(n):
            if n < 3:
                return n
            return rec(n - 1) + rec(n - 2)

        if n < 0:
            return None
        return rec(n)


print(Solution().staircase(-1))
# None
print(Solution().staircase(4))
# 5
print(Solution().staircase(5))
# 8
