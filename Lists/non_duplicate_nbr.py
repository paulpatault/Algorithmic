"""
Given a list of numbers, 
where every number shows up twice except for one number, 
find that one number.

Input: [4, 3, 2, 4, 1, 3, 2]
Output: 1
"""


class Solution:
    def singleNumber(self, arr):
        """
            n = 0
            double = {}
            for elt in arr:
                if double.get(str(elt)):
                    double[str(elt)] = double.get(str(elt)) + 1
                    print(double)
                else:
                    double.setdefault(str(elt), 1)
            return n
        """
        res = arr[0]
        n = len(arr)
        for i in range(1, n):
            res = res ^ arr[i]
        return res


arr = [4, 3, 2, 5, 4, 3, 2]
sol = Solution().singleNumber(arr)
print("must be 5:", sol)

