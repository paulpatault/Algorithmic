"""
Given a list of numbers with only 3 unique numbers (1, 2, 3), sort the list in O(n) time.

Input: [3, 3, 2, 1, 3, 2, 1]
Output: [1, 1, 2, 2, 3, 3, 3]

"""


class Solution:
    def sortNums(self, arr):
        res = []
        for e in arr:
            if not e in res:
                res.append(e)
                print(res)
        res.sort()
        return [val for val in res for _ in (0, 1)]


arr = [3, 3, 2, 1, 3, 2, 1]
print(Solution().sortNums(arr))
# [1, 1, 2, 2, 3, 3, 3]
