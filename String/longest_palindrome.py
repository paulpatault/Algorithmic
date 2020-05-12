'''
A palindrome is a sequence of characters that reads the same backwards and forwards. 
Given a string, s, find the longest palindromic substring in s.

Input: "banana"
Output: "anana"

Input: "million"
Output: "illi"
'''

class Solution:
	def substring(self, start, end, s):
		if start > end or end > len(s): 
			return None
		return s[start:end+1]

	def isPalindrome(self, s):
		return s == s[::-1]

	def longestPalindrome(self, s, verbose=False):
		if self.isPalindrome(s): 
			return s
		mon_max = 0
		len_s = len(s)
		memo = ""
		for idx in range(0, len_s - mon_max + 1): 
			for idx2 in range(idx, len_s - mon_max + 1):
				sub = self.substring(idx, idx2, s)
				if verbose:
					print(sub)
				if self.isPalindrome(sub): 
					if mon_max < len(sub): 
						mon_max = len(sub)
						memo = sub
		return memo



l = [2, 7, 11, 15]
l2 = [9, 15, 3, 7]
k = 9

# Test program
s = "fracecar"
print(str(Solution().longestPalindrome(s)))
# racecar
