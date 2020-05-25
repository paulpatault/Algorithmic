"""
Given a sorted array, A, with possibly duplicated elements, 
find the indices of the first and last occurrences of a target element, x. 
Return -1 if the target is not found.

    Input: A = [1,3,3,5,7,8,9,9,9,15], target = 9
    Output: [6,8]

    Input: A = [100, 150, 150, 153], target = 150
    Output: [1,2]

    Input: A = [1,2,3,4,5,6,10], target = 9
    Output: [-1, -1]
"""


class Solution(object):
    def getRange(self, arr, target):
        for idx, elt in enumerate(arr):
            if elt == target:
                if arr[idx + 1] != target:
                    return [idx, idx]
                n = idx + 1
                next_ = arr[n]
                while next_ == target:
                    n += 1
                    next_ = arr[n]
                return [idx, n - 1]
        return [-1, -1]


# Test program
arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8]
x = 2
print(Solution().getRange(arr, x))
# [1, 4]
