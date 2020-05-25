"""
Given a string, find the length of the longest substring without repeating characters.
"""


class Solution:
    def lengthOfLongestSubstring(self, s):
        mmax = 0
        temp = 0
        liste = []
        for e in s:
            if not e in liste:
                liste.append(e)
                temp += 1
            else:
                liste = []
                liste.append(e)
                temp = 1
            mmax = max(mmax, temp)
        return mmax


print(Solution().lengthOfLongestSubstring("dvdf"))
# 10
