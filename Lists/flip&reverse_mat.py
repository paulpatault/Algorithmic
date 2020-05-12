"""
Given a binary matrix A, we want to flip the image horizontally, 
then invert it, and return the resulting image.

To flip an image horizontally means that each row of the image is reversed.  
For example, flipping [1, 1, 0] horizontally results in [0, 1, 1].

To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0. 
For example, inverting [0, 1, 1] results in [1, 0, 0].

Input: [[1,1,0],[1,0,1],[0,0,0]]
Output: [[1,0,0],[0,1,0],[1,1,1]]

Input: [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
Output: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
"""


class Solution:
    def flipAndInvertImage(self, A):
        for i, mat in enumerate(A):
            for j, elt in enumerate(mat):
                if elt == 1:
                    A[i][j] = 0
                else:
                    A[i][j] = 1
            A[i] = A[i][::-1]
        return A


l = [[1, 1, 0], [1, 0, 1], [0, 0, 0]]
eq = [[1, 0, 0], [0, 1, 0], [1, 1, 1]]
l = Solution().flipAndInvertImage(l)
print(l == eq)

l = [[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]
eq = [[1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 0, 1], [1, 0, 1, 0]]
l = Solution().flipAndInvertImage(l)
print(l == eq)
