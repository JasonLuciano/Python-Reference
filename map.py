nums = [1, -5, 7.25, 99]

for num in nums:
	print(num * 4)

new_nums = [num*4 for num in nums]
print(new_nums)


def new_func(num):
	if num > 5:
		num = num + 4
	else:
		num = num - 4

	return num**2

for new_num in map(new_func, nums):
	print(new_num)

# convert to list
convert_to_list  = list(map(new_func, nums))
print(convert_to_list)


names = ['Savvy', 'Bryndle', 'Basil', 'Ed']
def handle_names(name):
	name = name.lower()
	if name == "savvy":
		return "Brindled"
	elif name == 'bryndle':
		return 'Brown'
	elif name == 'basil':
		return 'At the pound.'
	elif name == 'ed':
		return "This is a a horse of course"
	else:
		return "Don't Know"

description = list(map(handle_names, names))
print(description)