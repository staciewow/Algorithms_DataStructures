class Solution():
	'''
	Given a non-empty string s, you may delete at most one character. 
	Judge whether you can make it a palindrome
	'''
	def validPalindrome(self, s):

		def isPalindrome(s, left, right):
			while left < right:
				if s[left] != s[right]:
					return False
				left += 1
				right -= 1
			return True


		left, right = 0, len(s) - 1
		while left < right:
			while left < right and not self.isValid(s[left]):
				left += 1
			while left < right and not self.isValid(s[right]):
				right -= 1

			if s[left] == s[right]:
				left += 1
				right -= 1
			else:
				if isPalindrome(s, left + 1, right):  ## skip 1 on left, check the rest
					return True
				if isPalindrome(s, left, right -1):  ## skip 1 on right, check the rest
					return True
				return False
		return True

	def isValid(self, letter):
		return letter.isdigit() or letter.isalpha()



s1 = "atbbga"
s2 = 'abadaa'
s3 = 'abada.a'
print(Solution().validPalindrome(s1), Solution().validPalindrome(s2),
	Solution().validPalindrome(s3))
