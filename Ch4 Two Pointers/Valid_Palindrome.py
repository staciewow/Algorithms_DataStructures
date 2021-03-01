class Palindrome:
	def isPalindromeNbr(self, x):
		'''
		Given an integer x, return true if x is palindrome integer.
		An integer is a palindrome when it reads the same backward as forward.
		For example, 121 is palindrome while 123 is not. 
		if the integer is negative, return False
		'''
		if x < 0:
			return False
		x = str(x)
		left, right = 0, len(x) - 1
		while left < right:
			if x[left] != x[right]:
				return False
			else:
				left += 1
				right -= 1
		return True


	def isPalindromeString(self, s):
		'''
		similar to Palindrome nbr, aba is Palindrome while abc is not
		exclude non-digits and non-alphas
		'''
		left, right = 0, len(s) - 1
		while left < right:
			while left < right and not self.isValid(s[left]):
				left += 1
			while left < right and not self.isValid(s[right]):
				right -= 1
			if left < right and s[left].lower() != s[right].lower():
				return False
			left += 1
			right -= 1
		return True 


	def isValid(self, letter):
		return letter.isdigit() or letter.isalpha()


x1 = 131
x2 = 132
print(Palindrome().isPalindromeNbr(x1), Palindrome().isPalindromeNbr(x2))


s1 = 'A man, a plan, a canal: Panama'
s2 = 'race a car'
print(Palindrome().isPalindromeString(s1), Palindrome().isPalindromeString(s2))