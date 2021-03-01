## leetcode 912

class Solution:

	def sortArray(self, array):
		left, right = 0, len(array) - 1
		self.quickSort(array, left, right)
		return array

	# def quickSort(self, array, left, right):
	# 	if left >= right: 
	# 		return 
	# 	i = left + 1
	# 	j = right
	# 	while i <= j:
	# 		while i <= j and array[i] <= array[left]:
	# 			i += 1
	# 		while i <= j and array[j] >= array[left]:
	# 			j -= 1
	# 		if i < j:
	# 			array[i], array[j] = array[j], array[i]
	# 	array[left], array[j] = array[j], array[left]

	# 	self.quickSort(array, left, j-1)
	# 	self.quickSort(array, j+1, right)


	def quickSort(self, array, start, end):
		if start >= end:
			return
		left, right = start, end 
		pivot = array[(start + end) / 2]  ##pivot is a value, not an index
		while left <= right:
			while left <= right and array[left] < pivot:
				left += 1
			while left <= right and array[right] > pivot:
				right -= 1
			if left <= right:
				array[left], array[right] = array[right], array[left]
				left += 1
				right -= 1
		# array[left], array[right] = array[right], array[left]

		self.quickSort(array, start, right)
		self.quickSort(array, left, end)

a = [3,2,1, 2]
print(Solution().sortArray(a))