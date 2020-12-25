def filter_even_numbers(num):
	"""Return only even numbers"""
	return num % 2 == 0

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Long
for num in filter(filter_even_numbers, nums):
	print(num)

evens = list(filter(filter_even_numbers, nums))
print(evens)