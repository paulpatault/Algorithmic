'''
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
'''

class Solution:
    def addInList(self, liste, k): 
        for i, e in enumerate(liste):
            for j, e2 in enumerate(liste):
                if i == j :
                    pass
                elif e + e2 == k: 
                    return [i, j]
        return False


l = [2, 7, 11, 15]
l2 = [9, 15, 3, 7]
k = 9

print (Solution().addInList(l, k))
print (Solution().addInList(l2, k))