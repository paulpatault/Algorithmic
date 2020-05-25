class Solution:
    def nth(self, n: int, verbose=False):
        if n == 1:
            return "1"
        if n == 2:
            return "11"
        s = "11"
        for i in range(3, n + 1):
            if verbose:
                print(s)
            s += "$"
            l = len(s)
            cnt = 1
            tmp = ""
            for j in range(1, l):
                if s[j] != s[j - 1]:
                    tmp += str(cnt + 0)
                    tmp += s[j - 1]
                    cnt = 1
                else:
                    cnt += 1
            s = tmp
        return s


print(Solution().nth(6))
