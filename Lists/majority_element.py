class Solution:
    def majorityElt(self, arr):
        size = len(arr)
        if size == 1:
            return arr[0]
        double = {}
        for elt in arr:
            if double.get(str(elt)):
                double[str(elt)] = double.get(str(elt)) + 1
                if double.get(str(elt)) > size / 2:
                    return elt
            else:
                double.setdefault(str(elt), 1)


print(Solution().majorityElt([3, 2, 3]))
print(Solution().majorityElt([2, 2, 1, 1, 1, 2, 2]))
print(Solution().majorityElt([1]))

