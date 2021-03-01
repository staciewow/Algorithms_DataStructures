class Solution():
	'''
	Given a non-empty string s, you may delete at most 1 character.
	Judge whether you can make it a palindorm. 
	Solution II: leveraging the third function claled "find difference", which returns the location of left and right where the difference is.
	'''

	def ValidPalindrome(self, s):
		left, right = self.findDifference(s, 0, len(s) - 1)
		if left >= right:
			return True
		return self.isPalindrome(s, left + 1, right) or self.isPalindrome(s, left, right - 1)

	def isPalindrome(self, s, left, right):
		left, right = self.findDifference(s, left, right)
		return left >= right

	def findDifference(self, s, left, right):
		while left < right:
			if s[left] != s[right]:
				return left, right
			left += 1
			right -= 1
		return left, right



s1 = "atbbga"
s2 = 'abadaa'
s3 = 'abada.a'
print(Solution().ValidPalindrome(s1), Solution().ValidPalindrome(s2),
	Solution().ValidPalindrome(s3))

