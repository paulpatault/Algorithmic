"""
Given a 2D matrix of characters and a target word, 
write a function that returns whether the word can be found in the matrix 
by going left-to-right, or up-to-down.


For example, given the following matrix:

[['F', 'A', 'C', 'I'],
 ['O', 'B', 'Q', 'P'],
 ['A', 'N', 'O', 'B'],
 ['M', 'A', 'S', 'S']]

'FOAM'-> return true, since it's the leftmost column.
'MASS'-> return true, since it's the last row.
"""


class Solution:
    def isIn(self, mat, word):
        for e in mat:
            if word == "".join(e):
                return True

        for j in range(len(mat[0])):
            w = []
            for i in range(len(mat)):
                w.append(mat[i][j])
            if word == "".join(w):
                return True
        return False


mat = [
    ["F", "A", "C", "I"],
    ["O", "B", "Q", "P"],
    ["A", "N", "O", "B"],
    ["M", "A", "S", "S"],
]

print(Solution().isIn(mat, "FOAM"))  # true
print(Solution().isIn(mat, "MASS"))  # true
print(Solution().isIn(mat, "MADS"))  # false
print(Solution().isIn(mat, "FACI"))  # true
print(Solution().isIn(mat, "FAMI"))  # false
