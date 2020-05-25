"""
Given an array of numbers, 
find the length of the longest increasing sublist in the array. 

For example, given the array [12, 2, 10, 0, 1, 4, 8, 4, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15],
the longest increasing sublist has length 4: it is 0, 1, 4 and 8.
"""


class Solution:
    def incr_sub(self, arr):
        max_ = [1]
        for i in range(len(arr)):
            if i < len(arr) - 1:
                if arr[i + 1] > arr[i]:
                    max_[len(max_) - 1] += 1
                else:
                    max_.append(1)
        return max(max_)


arr = [12, 2, 10, 0, 1, 4, 8, 4, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
sol = Solution().incr_sub(arr)
print(sol)
