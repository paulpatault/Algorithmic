"""
You are given an array of integers in an arbitrary order. 
Return whether or not it is possible to make the array non-decreasing 
by modifying at most 1 element to any value.

We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).


Example:

[13, 4, 7] should return true, 
ince we can modify 13 to any value 4 or less, to make it non-decreasing.

[13, 4, 1] however, should return false, 
since there is no way to modify just one element to make the array non-decreasing.

"""


class Solution:
    def check(self, arr):
        nb = 0
        for idx in range(len(arr) - 1):
            if arr[idx] > arr[idx + 1]:
                nb += 1
            if nb > 1:
                return False
        return True


arr = [13, 4, 7]
print(Solution().check(arr))
# True
arr = [5, 1, 3, 2, 5]
print(Solution().check(arr))
# False
