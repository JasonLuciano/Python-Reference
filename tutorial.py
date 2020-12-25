# Files
# with open("write_file_text.txt", "w") as f:
# 	f.write("Hello World of file writing")
# 	f.close()

# with open("write_file_text.txt", "r") as f:
# 	print(type(f))
# 	contents = f.read()
# 	f.close()

# 	print(contents)

# with open("write_file_text.txt", "a") as f:
# 	f.write("\nThis is line 4")
# 	f.close()


# with open("write_file_text.txt", "r") as f:
# 	print("f.name => ", f.name)
# 	lines = f.read()
# 	f.close()

# 	print(lines)

# 	for line in lines:
# 		print(line)


# Comparison Operators

name = "Jason" 

if name == 'Jason':
	print(f"Name is Jason")

# Comparison Shortcuts
# If len string, List, Tuple, Set, Dictionary == 0 then False, If len string gt 0 then True
# None is always false in Py
# Always use == when comparing num or string, use None when looking for None 
string = "" 

if string:
	print("String has value")
if not string:
	print("String does not have value")
bool(string) = False 

if total == None:
	print("== none")

if total is None
	print("is none")

lst = ['Hello']
lst2 = ['Hello']

if lst == lst2
	print("Both lists are the same.");


# Multiple Comparison Oerators
course = "Python"
student = "Jason"
grade = 12

if course == "Python" and student == "Jason":
	print(f"Welcome to { course }, {student}")

if (course == "Python" and student == "Jason") or grade == 12:
	print(f"Welcome to { course }, {student}")

# Chaining Operators Together
name = "Jason"

if name == "Jason":
	print(name)
elif name == "Savvy":
	print(name)
elif name == "Paula":
	print(name)
else:
	print("No matches")

# Loops
# For (loops all), While (will stop when meets certain criteria)
word = "Computer"
for letter in word:
	print(letter) 

num = 1
while num <= 100:
	print(num)
	num = num + 1

# For Loop
pets = ['Cat', 'Dog', 'Bird', 'Goat'] 

for animal in pets:
	animal = animal.replace("a", "4").replace("o", "0").replace("i", "!")
	print(f"The animal with funky letters is { animal }")

pets = {'Cat', 'Dog', 'Bird', 'Goat'}

for set_animal in pets:
	print(f"The animal is {set_animal}")

# Tuple of Tuples
people = (
	(30, "Jason"),
	(10, "Savvy"),
	(56, "Paula")
)
print(people)

for age, name in people:
	print(f"{name} is {age} years old")

# Looping through Dictionaries
people = {
	'name': 'Jason',
	'course': 'Python',
	'role': 'Developer'
}

for key, value in people.items():
	print(f"Key = {key} \t\t Value = {value}")

# While Loops / CTRL C to break if in CMD 
num = 100
while num > 0:
	print(num)
	num = num - 5

# Break and Continue
colors = ('Blue', 'Green', 'Yellow', 'Orange', 'Red', 'Purple')

# Exclude Orange, but continues to include other colors
for color in colors:
	if color == 'Orange':
		continue 
	print(color+ '\n')

# Exclude Orange and remaining colors:
print("Starting Loop")
for color in colors:
	if color == 'Orange':
		break
	print(color + '\n')
print("Ending Loop")

while True:
	name = input("Guess my name:\n")
	if name.lower() == "henry":
		print("YOU WIN")
		break
	print('That was the wrong name...try again.')

# Type Casting / if you need to replace 5 with 4
tup = (1, 2, 3, 5)
lst = list(tup)
lst[3] = 4
tup = tuple(lst)
print(tup)

# Boolean
name = input("What is your name")
has_name = bool(name)

if has_name:
	print("This name is ", name)

# Remove Duplicates
groceries = list(set(['Milk', 'Eggs', 'Bread', 'Milk']))
print(groceries)

# Helpful Operators
# in
'python' in 'python for everbody'

if 'jason' in ['savvy', 'jason']:
	print('Yes, in list')
else:
	print('not list')

# enum / enumerate
languages = ['ColdFusion', 'Java', 'Python', 'C++']

for index, lang in enumerate(languages):
	# print(index, lang)
	print(index + 1, lang)

# zipping / merge 2 lists to tuple
list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]

for item in zip(list1, list2):
	print(item)

for letter, number in zip(list1, list2):
	print(letter, " => ", number)

# min(), max()
print(min(list1))
print(min(list2))

# join()
print(':'.join(list1))

# split()
course = 'Python for Everybody'

words = course.split(' ')
print(words)
# Alphabetical by case
words.sort()

course = '_'.join(words) # Python_for_Everybody

# import
from random import shuffle
print(words)

# List Comprehensions
course = "Python for Everybody"

mylist = []
for letter in course:
	mylist.append(letter)

print(mylist)
# Same result from above with less code
mylist2 = [letter for letter in course]
print(mylist2)


vowels = [letter for letter in course if letter.lower() in 'aeiou']
print(vowels)

numbers = [num **2 for num in range(0,9)]
print(numbers)

# long convert celcious to farenheit
f = []
c = [-40, -20, 0, 10, 15, 25, 35]

for temp in c:
	temp = (temp*1.8 + 31)
	f.append(temp)
print(f)

# shortcut / convert celcious to farenheit
c = [-40, -20, 0, 10, 15, 25, 35]
f = [(temp*1.8) +32 for temp in c]
print(f)

# Dictionary Comprehensions
# long
keys = ['name', 'age', 'title']
values = ['Jason', 28, 'Developer']

person = {}
for key, value in zip(keys, values):
	person[key] = value

print(person)

# short
person2 = {
	key:value for key, value in zip(keys, values)
}
print(person2)

person3 = {
	key:value for key, value in zip(keys, values) if key != 'age'	
}
print(person2)
