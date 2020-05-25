import random as rd

import sys

sys.setrecursionlimit(100000)


class Solution:
    def monte_carlo(self, p, cpt):
        if cpt == 0:
            return 4 * p / 10000
        x = rd.uniform(0, 1)
        y = rd.uniform(0, 1)
        c = 0
        if (x ** 2 + y ** 2) < 1:
            c = 1
        return round(self.monte_carlo(p + c, cpt - 1), 3)


a = Solution().monte_carlo(0, 10000)

print(a)

